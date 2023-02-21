# class Game:
#     def __init__(self):
#         self.selected_game = 0
#         self.selected_level = 0
import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\n\
Hello and welcome to the World of Games (WoG).\n\
Here you can find many cool games to play.\n")


def load_game(**game):
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n\
2. Guess Game - guess a number and see if you chose like the computer.\n\
3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")

    s_game = game.get('selected_game')
    s_level = game.get('selected_level')

    while int(s_game) < 1 or int(s_game) > 3:
        s_game = input("Please choose a game to play (1,2,3):")
        if not s_game.isnumeric():
            s_game = 0
            print("Please enter only numeric option 1,2,3")
    while int(s_level) < 1 or int(s_level) > 5:
        s_level = input("Please choose game difficulty from 1 to 5:")
        if not s_level.isnumeric():
            s_level = 0
            print("Please enter only numeric option for difficulty 1,2,3,4,5")
    # print(s_game, s_level)
    s_game = {"selected_game": s_game}
    s_level = {"selected_level": s_level}
    game.update(s_game)
    game.update(s_level)

    return game


while True:
    f_name = input("Hello, What is your name?")
    welcome(f_name)
    new_game = load_game(selected_game=0, selected_level=0)
    new_game_selection = new_game.get('selected_game')
    new_level_selection = new_game.get('selected_level')
    if int(new_game_selection) == 1:
        result = MemoryGame.play(int(new_level_selection))
    elif int(new_game_selection) == 2:
        result = GuessGame.play(int(new_level_selection))
    elif int(new_game_selection) == 3:
        result = CurrencyRouletteGame.play(int(new_level_selection))
    # If the user win the game invoke the score
    if result:
        Score.add_score(int(new_level_selection))

