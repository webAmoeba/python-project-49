from brain_games.games.template import run_template, get_random_number


def play():
    title = 'What number is missing in the progression?'
    return run_template(title, generate_question_and_answer)


def generate_question_and_answer():
    start = get_random_number(1, 50)
    step = get_random_number(2, 50)
    length = get_random_number(5, 10)
    arr = []

    for _ in range(length):
        arr.append(start.__str__())
        start += step

    empty = get_random_number(1, length - 2)
    result = arr[empty]
    arr[empty] = '..'
    question = ' '.join(arr)

    return question, result.__str__()
