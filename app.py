def welcome():
    username = input('Enter your username: ')
    print(f'Hi {username} and welcome to the World Of Games: The Epic Journey!')

def start_play():
    while True:
        games = """1. Memory Game
2. Guess Game
3. Currency Roulette
"""
        print(games)

        choose_game = input('Enter a game number: ')
        if not choose_game.isdigit() or int(choose_game) not in [1, 2, 3]:
            print('Out of range. Please enter a number between 1 and 3.')
            continue

        choose_game = int(choose_game)  # Now we know it's a valid number

        difficulty = input('Choose a difficulty level between 1-5: ')
        if not difficulty.isdigit() or not (1 <= int(difficulty) <= 5):
            print('Difficulty level out of range. Please enter a number between 1 and 5.')
            continue

        difficulty = int(difficulty)  # Now we know it's a valid number


        return choose_game, difficulty

def play_game():
    welcome()  #WELCOME TO PLAYER
    while True:
        game_number, difficulty = start_play()  #CHOOSING GAME AND DIFFICULTY LEVEL

        # שחק את המשחק לפי הבחירה
        if game_number == 1:
            from games.memory_game import play as play_memory_game
            play_memory_game(difficulty)
        elif game_number == 2:
            from games.guess_game import play as play_guess_game
            play_guess_game(difficulty)
        elif game_number == 3:
            from games.currency_roulette_game import play as play_currency_roulette
            play_currency_roulette(difficulty)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
