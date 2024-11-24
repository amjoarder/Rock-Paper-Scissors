import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("\nEnter your choice (rock, paper, scissors): ").strip().lower()
    if choice in ["rock", "paper", "scissors"]:
        return choice
    else:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return None

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        
        if user_choice is None:
            continue
        
        print(f"\nComputer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
