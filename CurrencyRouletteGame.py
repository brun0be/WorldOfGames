import numpy as np
import requests
from numpy import random


def get_money_interval(difficulty):
    num = random.randint(low=1, high=101, size=1)
    num = num.item()
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount={num}"

    payload = {}
    headers = {
      "apikey": "L4HaHP26ftE1YVnbkCSPQDwxXKHG7OxU"
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    json_data = response.json()
    if status_code == 200:
        amount = json_data['result']
        # print(num, amount)
    else:
        print("We faced an issue with the exchange service.")
    interval = 6 - difficulty
    guess = {'num': num, 'amount': amount, 'min': int(amount)-interval, 'max': int(amount)+interval}

    return guess


def get_guess_from_user(guess):
    value = guess['num']
    low = guess['min']
    high = guess['max']

    user_guess = input(f'Enter your guess exchange for {value} from USD to ILS?')
    if int(user_guess) in range(low, high):
        print("You win!!")
    else:
        print("Too bad, you loose, next time")


def play(difficulty):
    guess = get_money_interval(difficulty)
    get_guess_from_user(guess)


