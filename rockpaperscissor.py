import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors'. Type 'quit' to exit.\n")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print("\nGame Over!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, result)
        print(f"Score: You {user_score} - {computer_score} Computer\n")



if __name__ == "__main__":
    play_game()
