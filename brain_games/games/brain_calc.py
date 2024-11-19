from brain_games.games.template import run_template, get_random_number


def play():
    title = 'What is the result of the expression?'
    return run_template(title, generate_question_and_answer)


def generate_question_and_answer():
    number1 = get_random_number()
    number2 = get_random_number()
    operations = '+-*'
    operation = operations[get_random_number(0, operations.__len__() - 1)]
    result = eval(f'{number1} {operation} {number2}')
    return f"{number1} {operation} {number2}", result.__str__()
