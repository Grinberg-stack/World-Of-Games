import os
import platform

# קבועים
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1
def screen_cleaner():


    os.system('cls' if platform.system() == 'Windows' else 'clear')
