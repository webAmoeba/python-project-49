from brain_games.scripts.template import play_game, get_random_number


def main():
    title = 'What is the result of the expression?'
    return play_game(title, generate_question_and_answer)


def generate_question_and_answer():
    number1 = get_random_number()
    number2 = get_random_number()
    operations = '+-*'
    operation = operations[get_random_number(0, operations.__len__() - 1)]
    result = eval(f'{number1} {operation} {number2}')
    return f"Question: {number1} {operation} {number2}", result.__str__()
