import random
import requests
from score import add_score  # ייבוא הפונקציה להוספת ניקוד

def get_money_interval(difficulty):
    """Retrieves the current USD to ILS exchange rate and calculates the acceptable range."""
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    exchange_rate = data['rates']['ILS']

    # Generate a random number between 1 and 100
    secret_usd_amount = random.randint(1, 100)

    # Calculate the value in ILS
    correct_value_ils = secret_usd_amount * exchange_rate

    # Calculate the acceptable range
    allowed_difference = 10 - difficulty
    lower_bound = correct_value_ils - allowed_difference
    upper_bound = correct_value_ils + allowed_difference

    return secret_usd_amount, lower_bound, upper_bound

def get_guess_from_user():
    """Prompts the user to input a guess for the converted value."""
    while True:
        try:
            guess = float(input("Guess the value in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_results(lower_bound, upper_bound, user_guess):
    """Checks if the user's guess is within the acceptable range."""
    return lower_bound <= user_guess <= upper_bound

def play(difficulty):
    """Executes the game and returns True if the user wins, False if they lose."""
    secret_usd_amount, lower_bound, upper_bound = get_money_interval(difficulty)
    print(f"You are guessing the value of ${secret_usd_amount} in ILS.")

    user_guess = get_guess_from_user()

    if compare_results(lower_bound, upper_bound, user_guess):
        print("Congratulations! Your guess is within the acceptable range!")
        # הוספת ניקוד
        new_score = add_score(difficulty)
        print(f"Your new score is: {new_score}")
        return True
    else:
        print(
            f"Sorry, the correct value was between {lower_bound:.2f} and {upper_bound:.2f} ILS. Better luck next time!")
        return False
