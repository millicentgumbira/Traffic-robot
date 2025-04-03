import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("\n=== ROCK, PAPER, SCISSORS ===")
    print("Play against the clare!")
    
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("0. Exit")
        
        choice = input("\nYour choice (0-3): ")
        
        if choice == "0":
            print("\nThanks for playing!")
            break
            
        if choice not in ["1", "2", "3"]:
            print("\nInvalid choice. Try again.")
            continue
            
        millie_move = options[int(choice) - 1]
        clare_move = random.choice(options)
        
        print(f"\nmillie chose: {millie_move.upper()}")
        print(f"clare chose: {clare_move.upper()}")
        
        if millie_move == clare_move:
            print("\nIt's a TIE!")
        elif ((millie_move == "rock" and clare_move == "scissors") or
              (millie_move == "paper" and clare_move == "rock") or 
              (millie_move == "scissors" and clare_move == "paper")):
            print("\nYOU WIN!")
        else:
            print("\nclare wins!")

if __name__ == "__main__":
    play_game()