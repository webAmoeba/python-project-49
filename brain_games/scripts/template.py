import random
import prompt
from brain_games.cli import welcome_user
from colorama import init, Fore, Style
init(autoreset=True)

MIN = 1
MAX = 99
ATTEMPTS = 3


def get_random_number(a=MIN, b=MAX):
    return random.randint(a, b)


def play_game(title, generate_question_and_answer):
    name = welcome_user()

    print(title)

    for _ in range(ATTEMPTS):
        question, correct_answer = generate_question_and_answer()
        print(question)
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(Fore.RED + f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'")
            return

        print(Fore.GREEN + 'Correct!')

    print(Fore.CYAN + Style.BRIGHT + f'Congratulations, {name}!')
