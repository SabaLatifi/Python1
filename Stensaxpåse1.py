import random


choices = ['rock', 'paper', 'scissors']

def get_player_choice():
    while True:
        player_choice = input("rock, paper or scissors? ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid input! Please choose from: rock, paper or scissors.")


def play_game():
    player_choice = get_player_choice()
    computer_choice = random.choice(choices)

    print(f"\nPlayer: {player_choice}")
    print(f"Computer: {computer_choice}")
    
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("Player wins mohahah!")
    else:
        print("Computer wins, welcome to the matrix!")

    print("Game over!\n")


play_game()
