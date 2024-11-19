from brain_games.games.template import run_template, get_random_number


def play():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return run_template(title, generate_question_and_answer)


def generate_question_and_answer():
    random_number = get_random_number(1, 103)
    result = 'yes' if is_prime(random_number) else 'no'
    return random_number, result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
