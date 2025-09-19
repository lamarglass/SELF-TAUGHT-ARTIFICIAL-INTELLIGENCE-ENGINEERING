# Documented-By-Lamar
from name_art import print_name

print_name() 

# name_art.py
import pyfiglet

def print_name(name="Documented By Lamar", font="banner3-D"):
    """
    Prints the given name in ASCII art.
    Default: "Lamar" with banner3-D font.
    """
    ascii_art = pyfiglet.figlet_format(name, font=font)
    print(ascii_art)

# Documented-By-Lamar
from name_art import print_name

print_name() 