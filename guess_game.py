# guess_game.py

import random
from score import add_score

def generate_number(difficulty):
    return random.randint(0, difficulty * 20)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Please enter a number between 0 and {difficulty * 20}: "))
            if 0 <= guess <= difficulty * 20:
                return guess
            else:
                print(f"Invalid input. The number must be between 0 and {difficulty * 20}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_results(secret_number, user_guess):
    return secret_number == user_guess

def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)

    if compare_results(secret_number, user_guess):
        print("Congratulations! You've guessed the correct number!")
        add_score(difficulty)  # הוספת ניקוד
        return True
    else:
        print(f"Sorry, the correct number was {secret_number}. Better luck next time!")
        return False
