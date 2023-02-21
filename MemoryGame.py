from numpy import random
from time import sleep
import os


def generate_sequence(difficulty):
    gen_seq = random.randint(low=1, high=101, size=difficulty)
    print(gen_seq, flush=True)
    sleep(0.7)
    os.system('clear')
    return gen_seq


def get_list_from_user():
    user_list = []
    lst = input('Enter the numbers you remember?')
    lst = lst.split()
    for i in lst:
        user_list.append(int(i))
    return user_list


def is_list_equal(list1, list2):
    if len(list1) != len(list2) or len(list2) == 0:
        print("Too bad, you loose, next time")
        return False

    comparison = [i == int(j) for i, j in zip(list1, list2)]
    if all(comparison):
        print("You win!!")
        return True
    else:
        print("Too bad, you loose, next time")
        return False


def play(difficulty):
    seq = generate_sequence(difficulty)
    # print(seq)
    user_numbers = get_list_from_user()
    # print(user_numbers)
    game_result = is_list_equal(seq, user_numbers)
    return game_result


