import sys
import os


def clear_screen():
    """Clears the screen by printing newlines."""
    os.system("cls" if os.name == "nt" else "clear")
    print()
