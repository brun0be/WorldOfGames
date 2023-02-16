import numpy as np
from numpy import random
from time import sleep
import sys
import os


def generate_sequence(difficulty):
    gen_seq = random.randint(low=1, high=101, size=difficulty)
    print(gen_seq, flush=True)
    sleep(0.7)
    os.system('clear')
    return gen_seq


def get_list_from_user():
    user_list = input('Enter the numbers you remember?')
    return user_list


def is_list_equal(list1, list2):
    comparison = [i == int(j) for i, j in zip(list1, list2)]
    if all(comparison):
        print("You win!!")
    else:
        print("Too bad, you loose, next time")


def play(difficulty):
    seq = generate_sequence(difficulty)
    # print(seq)
    user_numbers = get_list_from_user()
    # print(user_numbers)
    user_numbers = user_numbers.split()
    is_list_equal(seq, user_numbers)



