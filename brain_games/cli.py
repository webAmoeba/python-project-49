import prompt
from colorama import init, Fore, Style
init(autoreset=True)


def welcome_user():
    print(Style.BRIGHT + Fore.MAGENTA + "Welcome to the Brain Games!")
    name = prompt.string("May I have your" + Fore.YELLOW + " name? " + Style.RESET_ALL)
    print(f"Hello, {name}!")
    return name
