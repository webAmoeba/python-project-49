import random
import prompt
from brain_games.cli import welcome_user


def calc():
    attempts = 3
    name = welcome_user()
    operations = '+-*'

    print('What is the result of the expression?')

    for _ in range(attempts):
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operation = random.randint(0, operations.__len__() - 1)
        result = eval(f'{number1} {operations[operation]} {number2}')
        print(f"Question {number1} {operations[operation]} {number2}")
        answer = prompt.string("Your answer: ")

        if answer != result.__str__():
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
