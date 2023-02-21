from numpy import random


def generate_number(difficulty):
    return random.randint(difficulty)


def get_guess_from_user(difficulty):
    guess_number = input(f"Guess number between 0 to {difficulty}?:")
    return guess_number


def compare_results(number1, number2):
    if number1 == number2:
        print("You win!!")
        return True
    else:
        print("Too bad, you loose, next time")
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    # print(secret_number)
    user_number = get_guess_from_user(difficulty)
    # print(user_number)
    game_result = compare_results(secret_number, int(user_number))
    return game_result

