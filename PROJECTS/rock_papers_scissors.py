import random

print("Welcome to Rock, Papers, Scissors! Make your selection!")

options = ["rock","paper","scissor"]
computer_choice = random.choice(options)

player_input = input().strip().lower()

if player_input == "rock":
    player_move = "rock"

elif player_input == "paper":
    player_move = "paper"

elif player_input == "scissor":
    player_move = "scissor"

else:
    print("Invalid Choice!")
    exit()

# compares the moves

win = "You won!"
tie = "Tie! try again."
lose = "You lost!"

if player_move == computer_choice:
    print(tie)

elif player_move == "rock" and computer_choice == "scissor":
    print(win)

elif player_move == "paper" and computer_choice == "rock":
    print(win)

elif player_move == "scissor" and computer_choice == "paper":
    print(win)

else:
    print(lose)
    


