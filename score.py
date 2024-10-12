from utils import SCORES_FILE_NAME

# קבועים
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    """מוסיף ניקוד על פי רמת הקושי למשחק."""
    try:

        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read().strip())
    except FileNotFoundError:
        # אם הקובץ לא קיים, נתחיל מניקוד של 0
        current_score = 0
    except ValueError:
        # אם יש בעיה בקריאת הניקוד, נתחיל מניקוד של 0
        current_score = 0


    new_score = current_score + POINTS_OF_WINNING(difficulty)


    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))

    return new_score  # מחזיר את הניקוד החדש
