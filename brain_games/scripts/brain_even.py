import random
import prompt


def is_even():
    random_number = random.randint(1, 99)
    even = 'yes' if random_number % 2 == 0 else 'no'
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f"Question: {random_number}")
    answer = prompt.string("Your answer: ")
    if answer != even:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{even}'")
