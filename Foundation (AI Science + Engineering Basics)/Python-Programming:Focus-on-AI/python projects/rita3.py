# Install dependencies (uncomment if running locally or in Colab)
# !pip install transformers torch

from transformers import pipeline

# Load a conversational model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Simple loop
print("🤖 NovaBot: Hi! I'm your AI chatbot. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("🤖 NovaBot: Goodbye! 👋")
        break

    response = chatbot(user_input)
    print(f"🤖 NovaBot:", response[0]['generated_text'])
