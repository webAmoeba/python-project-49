from brain_games.scripts.template import play_game, get_random_number


def main():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return play_game(title, generate_question_and_answer)


def generate_question_and_answer():
    random_number = get_random_number(1, 103)
    result = 'yes' if is_prime(random_number) else 'no'
    return f"Question: {random_number}", result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
