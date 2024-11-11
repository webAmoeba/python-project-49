from brain_games.scripts.template import play_game, get_random_number


def main():
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    return play_game(title, generate_question_and_answer)


def generate_question_and_answer():
    random_number = get_random_number()
    result = 'yes' if random_number % 2 == 0 else 'no'
    return f"Question: {random_number}", result
