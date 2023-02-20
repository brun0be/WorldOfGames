from flask import Flask, render_template

# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"

@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)