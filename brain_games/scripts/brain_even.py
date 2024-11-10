import random
import prompt
from brain_games.cli import welcome_user


def is_even():
    attempts = 3
    name = welcome_user()

    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(attempts):
        random_number = random.randint(1, 99)
        even = 'yes' if random_number % 2 == 0 else 'no'
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        if answer != even:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even}'")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
