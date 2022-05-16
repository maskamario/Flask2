from flask import Flask, render_template, request, redirect
from flask_session import Session
app = Flask(__name__)




nimekiri = []


@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        lause = request.form['sisu']
        nimekiri.append(lause)

    return render_template('index.html', nimekiri = nimekiri)




if __name__ == "__main__":
    app.run()