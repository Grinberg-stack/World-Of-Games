import random
import time
from utils import screen_cleaner
from score import add_score

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    while True:
        try:
            user_input = input(f"Enter the {difficulty} numbers separated by spaces: ")
            user_list = list(map(int, user_input.split()))

            if len(user_list) != difficulty:
                print(f"Please enter exactly {difficulty} numbers.")
                continue

            return user_list
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def is_list_equal(sequence, user_list):
    return sequence == user_list

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Remember the following sequence:")
    print(sequence)

    time.sleep(0.7)
    screen_cleaner()

    user_list = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_list):
        print("Congratulations! You remembered the sequence correctly!")
        add_score(difficulty)
        return True
    else:
        print(f"Sorry, the correct sequence was: {sequence}. Better luck next time!")
        return False
