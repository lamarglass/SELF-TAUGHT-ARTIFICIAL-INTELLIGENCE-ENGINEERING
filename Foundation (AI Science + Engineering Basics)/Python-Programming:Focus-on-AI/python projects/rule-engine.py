"""
rule_engine.py
Forward-chaining rule-based engine (simple, extensible).

Usage:
    python rule_engine.py                 # runs demo scenarios
    from rule_engine import RuleEngine    # to import into other code

Features:
- Rules can be loaded from YAML or provided as Python dicts.
- Conditions support operators: eq, ne, lt, le, gt, ge, in, contains.
- Actions support: recommend, set_fact, print_msg, call (callbacks), add_note.
- Optional 'single_fire' prevents a rule from firing more than once.
- Rules are prioritized by 'priority' (higher first).
"""
from typing import Any, Dict, List, Callable, Tuple
import yaml
import operator
import os

# ---------- Operators ----------
_OPERATORS = {
    "eq": operator.eq,
    "ne": operator.ne,
    "lt": operator.lt,
    "le": operator.le,
    "gt": operator.gt,
    "ge": operator.ge,
    "in": lambda a, b: a in b if isinstance(b, (list, tuple, set, str)) else False,
    "contains": lambda a, b: b in a if isinstance(a, (list, tuple, set, str)) else False,
}

# ---------- Engine ----------
class RuleEngine:
    def __init__(self, rules: List[Dict] = None, callbacks: Dict[str, Callable] = None, max_cycles: int = 100):
        self.rules = sorted(rules or [], key=lambda r: r.get("priority", 0), reverse=True)
        self.callbacks = callbacks or {}
        self.max_cycles = max_cycles

        # runtime
        self.facts: Dict[str, Any] = {}
        self.recommendations: List[str] = []
        self.notes: List[str] = []
        self.fired_rules: List[str] = []

    @classmethod
    def from_yaml(cls, path: str, callbacks: Dict[str, Callable] = None, max_cycles: int = 100):
        with open(path, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        rules = data.get("rules", data)  # allow file to be either {rules: [...]} or [...]
        return cls(rules=rules, callbacks=callbacks, max_cycles=max_cycles)

    def reset(self, facts: Dict[str, Any] = None):
        self.facts = dict(facts or {})
        self.recommendations = []
        self.notes = []
        self.fired_rules = []

    def _eval_condition(self, cond: Dict) -> bool:
        key = cond["fact"]
        op = cond.get("op", "eq")
        val = cond.get("value")

        if key not in self.facts:
            return False

        left = self.facts[key]
        fn = _OPERATORS.get(op)
        if fn is None:
            raise ValueError(f"Unsupported operator: {op}")
        try:
            return fn(left, val)
        except Exception:
            return False

    def _eval_conditions(self, conds: List[Dict]) -> bool:
        # default AND semantics. Support for OR groups could be added later.
        return all(self._eval_condition(c) for c in conds)

    def _perform_action(self, action: Dict) -> bool:
        t = action["type"]
        if t == "recommend":
            self.recommendations.append(action["value"])
            return False
        elif t == "set_fact":
            fact = action["fact"]
            value = action["value"]
            old = self.facts.get(fact, None)
            self.facts[fact] = value
            return old != value
        elif t == "print_msg":
            print(action["value"])
            return False
        elif t == "add_note":
            self.notes.append(action["value"])
            return False
        elif t == "call":
            fn_name = action["fn"]
            args = action.get("args", [])
            kwargs = action.get("kwargs", {})
            if fn_name in self.callbacks:
                try:
                    self.callbacks[fn_name](*args, **kwargs)
                except Exception as e:
                    print(f"[Callback Error] {e}")
            else:
                print(f"[Warning] Callback '{fn_name}' not found")
            return False
        else:
            print(f"[Warning] Unknown action type: {t}")
            return False

    def run(self, initial_facts: Dict[str, Any] = None) -> Tuple[Dict[str, Any], List[str], List[str]]:
        """Runs the engine until no new fact changes or max cycles reached.
        Returns (facts, recommendations, notes).
        """
        self.reset(initial_facts or {})
        cycles = 0
        changed = True

        while changed and cycles < self.max_cycles:
            cycles += 1
            changed = False
            for rule in self.rules:
                name = rule.get("name", "<unnamed>")
                single_fire = rule.get("single_fire", False)
                if single_fire and name in self.fired_rules:
                    continue

                conds = rule.get("conditions", [])
                conds_ok = True if not conds else self._eval_conditions(conds)

                if conds_ok:
                    for action in rule.get("actions", []):
                        action_changed = self._perform_action(action)
                        if action_changed:
                            changed = True
                    self.fired_rules.append(name)
        return self.facts, self.recommendations, self.notes

# ---------- Example callback ----------
def open_resource(url: str):
    print(f"[Open resource] {url}")

# ---------- Demo ----------
if __name__ == "__main__":
    # try to load rules.yml from the same folder if exists
    cwd = os.path.dirname(__file__)
    yaml_path = os.path.join(cwd, "rules.yml")
    callbacks = {"open_resource": open_resource}

    if os.path.exists(yaml_path):
        engine = RuleEngine.from_yaml(yaml_path, callbacks=callbacks)
        print("Loaded rules from rules.yml\n")
    else:
        # fallback: a tiny built-in rule set
        sample_rules = [
            {
                "name": "foundations_recommend",
                "priority": 10,
                "conditions": [{"fact": "progress", "op": "lt", "value": 0.3}],
                "actions": [
                    {"type": "recommend", "value": "Focus on Foundations: Python, Math, Data Structures."},
                    {"type": "call", "fn": "open_resource", "args": ["https://realpython.com/"]},
                    {"type": "set_fact", "fact": "focus", "value": "foundations"}
                ],
                "single_fire": True
            }
        ]
        engine = RuleEngine(rules=sample_rules, callbacks=callbacks)

    # Example scenarios
    scenarios = {
        "fresh": {"progress": 0.1, "daily_hours": 5, "has_gpu": False, "stress_level": 3},
        "mid_busy": {"progress": 0.45, "daily_hours": 2, "has_gpu": False, "stress_level": 4},
        "ready_deep": {"progress": 0.75, "daily_hours": 4, "has_gpu": True, "stress_level": 2},
        "burnout": {"progress": 0.5, "daily_hours": 6, "has_gpu": False, "stress_level": 8},
    }

    for name, facts in scenarios.items():
        print("\n>>> Scenario:", name)
        facts_out, recs, notes = engine.run(facts)
        print("Facts after run:", facts_out)
        print("Recommendations:")
        for r in recs:
            print("  -", r)
        if notes:
            print("Notes:")
            for n in notes:
                print("  -", n)
