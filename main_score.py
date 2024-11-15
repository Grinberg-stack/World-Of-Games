from flask import Flask, render_template_string
import os

app = Flask(__name__)

SCORES_FILE_NAME = "Scores.txt"


def read_score():
    """Reads the current score from the scores file."""
    if not os.path.exists(SCORES_FILE_NAME):
        return 0  # אם הקובץ לא קיים, מחזירים 0
    with open(SCORES_FILE_NAME, "r") as file:
        try:
            return int(file.read().strip())  # מחזירים את הניקוד כשלם
        except ValueError:
            return 0  # אם הפורמט לא תקין, מחזירים 0


@app.route('/score')
def score_server():
    """Serves the score as HTML."""
    current_score = read_score()

    # HTML string to render with an ID on the score element
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Score</title>
    </head>
    <body>
        <h1>Your Current Score</h1>
        <p id="score">Your score is: <strong>{current_score}</strong></p>
    </body>
    </html>
    """

    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)
