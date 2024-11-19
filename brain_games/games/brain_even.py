from brain_games.games.template import run_template, get_random_number


def play():
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    return run_template(title, generate_question_and_answer)


def generate_question_and_answer():
    random_number = get_random_number()
    result = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, result
