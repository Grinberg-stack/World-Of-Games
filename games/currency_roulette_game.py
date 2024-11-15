import random
from score import add_score

EXCHANGE_RATE = 3.6  # USD to ILS exchange rate

def get_money_interval(difficulty):
    """
    Returns the acceptable range for the value of USD in ILS based on the difficulty.
    The calculation uses a fixed exchange rate.
    """
    # Generate a random USD amount between 1 and 100
    secret_usd_amount = random.randint(1, 100)

    # Convert the USD amount to ILS
    correct_value_ils = secret_usd_amount * EXCHANGE_RATE

    # Calculate the allowed range: the higher the difficulty, the smaller the range
    allowed_difference = 10 - difficulty  # The higher the difficulty, the smaller the tolerance
    lower_bound = correct_value_ils - allowed_difference
    upper_bound = correct_value_ils + allowed_difference

    return secret_usd_amount, lower_bound, upper_bound

def get_guess_from_user():
    """
    Prompts the user to input a guess for the converted value in ILS.
    Ensures the input is a valid number.
    """
    while True:
        try:
            # Prompt the user to input their guess
            guess = float(input("Guess the value in ILS: "))
            return guess
        except ValueError:
            # If the input is not a valid number, print an error message and ask again
            print("Invalid input. Please enter a valid number.")

def compare_results(lower_bound, upper_bound, user_guess):
    """
    Compares the user's guess with the acceptable range and checks if it's correct.
    """
    return lower_bound <= user_guess <= upper_bound

def play(difficulty):
    """
    Runs the currency roulette game. If the user wins, return True, otherwise return False.
    The user guesses the ILS value of a random USD amount, based on difficulty.
    """
    # Get the USD amount and the acceptable range in ILS
    secret_usd_amount, lower_bound, upper_bound = get_money_interval(difficulty)
    print(f"You are guessing the value of ${secret_usd_amount} in ILS.")

    # Get the user's guess
    user_guess = get_guess_from_user()

    # Compare the user's guess with the acceptable range
    if compare_results(lower_bound, upper_bound, user_guess):
        print("Congratulations! Your guess is within the acceptable range!")
        # If the user wins, add score and print the new score
        new_score = add_score(difficulty)
        print(f"Your new score is: {new_score}")
        return True
    else:
        print(
            f"Sorry, the correct value was between {lower_bound:.2f} and {upper_bound:.2f} ILS. Better luck next time!"
        )
        return False
