from app import welcome, start_play
from guess_game import play as play_guess_game
from memory_game import play as play_memory_game
from currency_roulette_game import play as play_currency_roulette

def main():
    welcome()
    while True:
        game_number, difficulty = start_play()

        if game_number == 1:
            play_memory_game(difficulty)
        elif game_number == 2:
            play_guess_game(difficulty)
        elif game_number == 3:
            play_currency_roulette(difficulty)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
