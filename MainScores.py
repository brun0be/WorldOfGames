from flask import Flask, render_template


app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


@app.route('/')
def index():
    score_file = open("scores.txt", "r+")
    current_score = score_file.readline()
    return render_template('index.html', score=current_score)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)
