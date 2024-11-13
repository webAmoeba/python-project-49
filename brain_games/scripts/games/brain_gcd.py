import math
from brain_games.scripts.template import play_game, get_random_number


def main():
    title = 'Find the greatest common divisor of given numbers.'
    return play_game(title, generate_question_and_answer)


def generate_question_and_answer():
    number1 = get_random_number(1, 9)
    number2 = get_random_number(1, 9)
    divisor = get_random_number(1, 9)

    number1 *= divisor
    number2 *= divisor

    result = math.gcd(number1, number2)

    return f"Question: {number1} {number2}", result.__str__()
