def welcome():
    username = input('Enter your username: ')
    print(f'Hi {username} and welcome to the World Of Games: The Epic Journey!')

def start_play():
    while True:
        try:
            games = """1. Memory Game
2. Guess Game
3. Currency Roulette
"""
            print(games)

            choose_game = int(input('Enter a game number: '))
            if choose_game not in [1, 2, 3]:
                print('Out of range. Please enter a number between 1 and 3.')
                continue

            difficulty = int(input('Choose a difficulty level between 1-5: '))
            if difficulty < 1 or difficulty > 5:
                print('Difficulty level out of range. Please enter a number between 1 and 5.')
                continue

            # החזרת מספר המשחק ורמת הקושי
            return choose_game, difficulty

        except ValueError:
            print('Invalid input. Please enter a valid integer.')

