import random
import time

# Constants
choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

def display_rules():
    # Display the rules of the game.
    print("\nGame Rules:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

def get_player_name():
    # Prompt the user to enter their name.
    while True:
        player_name = input("Enter your name: ").strip()
        if player_name:
            return player_name
        print("Name cannot be empty. Please enter your name.\n")
        
def get_game_settings():
    # Get the number of rounds and games per round from the user.
    while True:
        try:
            total_rounds = int(input("Enter the number of rounds: "))
            repetitions_per_round = int(input("Enter the number of games per round: "))
            return total_rounds, repetitions_per_round
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def select_difficulty_level():
    # Prompt the user to select a difficulty level.
    while True:
        print("\nSelect difficulty level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ('1', '2', '3'):
            return { '1': 'easy', '2': 'medium', '3': 'hard' }[choice]
        print("\nInvalid choice. Please enter 1, 2, or 3.")

def get_computer_choice(difficulty_level, user_choice):
    # Generate computer's choice based on the difficulty level.
    Beginner = ((user_choice + 1) % 3) + 1
    Expert = (user_choice % 3) + 1

    if difficulty_level == 'easy':
        return random.choice([Beginner, Expert, Beginner])
    elif difficulty_level == 'medium':
        return random.randint(1, 3)
    elif difficulty_level == 'hard':
        return random.choice([Expert, Expert, Beginner])

def get_user_choice():
    # Prompt the user to enter their choice.
    while True:
        print("Enter your choice:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ('1', '2', '3'):
            return int(choice)
        print("\nInvalid choice. Please enter 1, 2, or 3.")

def play_single_game(difficulty_level, user_choice):
    # Play a single game and determine the winner.
    computer_choice = get_computer_choice(difficulty_level, user_choice)
    
    print("Rock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    
    print(f"\nYour choice: {choices[user_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")
    
    if user_choice == computer_choice:
        print("It's a Draw!\n")
        return 'draw', 0, 0
    elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):
        print("Computer wins this game!\n")
        return 'computer', 0, 1
    else:
        print("You win this game!\n")
        return 'user', 1, 0

def display_round_scoreboard(user_score, computer_score):
    # Display the scores for the current round.
    print("\nRound Scoreboard:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}\n")

def display_overall_scoreboard(player_name, user_total_rounds_won, computer_total_rounds_won):
    # Display the overall scores.
    print("\nOverall Scoreboard:")
    print(f"Rounds won by {player_name}: {user_total_rounds_won}")
    print(f"Rounds won by Computer: {computer_total_rounds_won}\n")

def display_winner(winner, player_name):
    # Display the final winner of the game.
    if winner == 'user':
        print(f"Congratulations, {player_name}! You win the game!")
        print("Keep up the good work!")
    elif winner == 'computer':
        print(f"Computer wins the game. Better luck next time, {player_name}!")
    else:
        print(f"{player_name}, the game ends in a tie!")
        print("Keep going. It's the courage to continue that matters.")

# ----------------------------------------------------------------------------------------------------------

def play_game():
    display_rules()
    player_name = get_player_name()
    
    # Get the number of rounds and games per round
    total_rounds, repetitions_per_round = get_game_settings()

    # Initialize total rounds won by user and computer
    user_total_rounds_won = 0
    computer_total_rounds_won = 0
    
    difficulty_level = select_difficulty_level()
    
    # Play the specified number of rounds
    for round_num in range(1, total_rounds + 1):
        print(f"\nRound {round_num}:")
        
        # Initialize scores for the current round
        round_user_score = 0
        round_computer_score = 0
        
        # Play the specified number of games per round
        for _ in range(repetitions_per_round):
            user_choice = get_user_choice()
            result, user_score, computer_score = play_single_game(difficulty_level, user_choice)
            round_user_score += user_score
            round_computer_score += computer_score
        
        # Display the scoreboard for the current round
        display_round_scoreboard(round_user_score, round_computer_score)
        
        # Update the total rounds won based on the current round's scores
        if round_user_score > round_computer_score:
            user_total_rounds_won += 1
        elif round_computer_score > round_user_score:
            computer_total_rounds_won += 1
    
    # Display the overall scoreboard after all rounds are played
    display_overall_scoreboard(player_name, user_total_rounds_won, computer_total_rounds_won)
    
    # Determine and display the final winner of the game
    if user_total_rounds_won > computer_total_rounds_won:
        display_winner('user', player_name)
    elif user_total_rounds_won < computer_total_rounds_won:
        display_winner('computer', player_name)
    else:
        display_winner('draw', player_name)

    # Ask the user if they want to play again
    play_again = input("\nDo you wish to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("\nThanks for playing! Have a nice day.")

play_game()

#----------------------------------------------*****------------------------------------------------------
