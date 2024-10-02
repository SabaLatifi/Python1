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
    
    # Bestäm vinnaren
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("Player wins mohahah!")
    else:
        print("Computer wins, welcome to the matrix!")


def start_game():
    while True:
        play_game()
        play_again = input("\nPlay again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Game over!")
            break


start_game()
