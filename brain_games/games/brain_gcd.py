import math
from brain_games.games.template import run_template, get_random_number


def play():
    title = 'Find the greatest common divisor of given numbers.'
    return run_template(title, generate_question_and_answer)


def generate_question_and_answer():
    number1 = get_random_number(1, 9)
    number2 = get_random_number(1, 9)
    divisor = get_random_number(1, 9)

    number1 *= divisor
    number2 *= divisor

    result = math.gcd(number1, number2)

    return f"{number1} {number2}", result.__str__()
