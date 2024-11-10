import random
import prompt
from brain_games.cli import welcome_user


def operate(a, b, operation):
    match operation:
        case 0:
            return a + b
        case 1:
            return a - b
        case 2:
            return a * b


def get_symbol(operation):
    match operation:
        case 0:
            return '+'
        case 1:
            return '-'
        case 2:
            return '*'


def calc():
    attempts = 3
    name = welcome_user()

    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    for _ in range(attempts):
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operation = random.randint(0, 2)
        result = operate(number1, number2, operation)
        print(f"Question {number1} {get_symbol(operation)} {number2}")
        answer = prompt.string("Your answer: ")

        if answer != result.__str__():
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
