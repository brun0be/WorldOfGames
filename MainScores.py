import Utils
from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
filename = Utils.SCORES_FILE_NAME
error_code = Utils.BAD_RETURN_CODE


@app.route('/')
def index():
    try:
        score_file = open(filename, "r+")
        current_score = score_file.readline()
        return render_template('index.html', SCORE=current_score)
    except (OSError, Exception):
        return render_template('error.html', ERROR_CODE=error_code)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
