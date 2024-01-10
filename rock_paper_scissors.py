# This game was created so that I could better understand how randomise work in Python. Feel free to give feedback!
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_choices = [
    {"name": "rock", "image": rock, "beats": "scissors"},
    {"name": "paper", "image": paper, "beats": "rock"},
    {"name": "scissors", "image": scissors, "beats": "paper"},
]
GAME_ON = False


def play_game():
    global GAME_ON
    GAME_ON = True
    while GAME_ON is True:
        user_choice_input = input(
            "What do you choose? Rock, paper, or scissors?\n"
        ).lower()
        user_choice = None

        for choice in game_choices:
            if user_choice_input == choice.get("name"):
                user_choice = choice
                break
        if user_choice is None:
            print("Bruh, that wasn't one of the choices. Try again.")
            play_game()
        else:
            print("You chose:")
            print(user_choice.get("image"))

        computer_choice = game_choices[random.randint(0, 2)]
        print("Computer chose:")
        print(computer_choice.get("image"))

        if computer_choice.get("beats") == user_choice.get("name"):
            print("You lose!")
        elif computer_choice.get("name") == user_choice.get("beats"):
            print("You win!")
        else:
            print("It's a draw!")

        play_again = input("You finna play again? y/n\n").lower()
        GAME_ON = play_again == "y"


play_game()
