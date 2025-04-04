import random

# Function to get the player's choice
def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Get player's and computer's choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}\n")

        # Determine and print the result
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
