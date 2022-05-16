from flask import Flask, render_template, request, redirect
from flask_session import Session
import datastuff
app = Flask(__name__)




nimekiri = []


@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        lause = request.form['sisu']
        nimekiri.append(lause)

    return render_template('index.html', nimekiri = nimekiri)


@app.route('/sisestamine', methods = ['POST', 'GET'])
def sisestamine():
    return render_template('sisestamine.html')

@app.route('/sisestamine_success', methods = ['POST'])
def sisestamine_success():
    if request.method == 'POST':
        agent = datastuff.insert_agent(request.form['full_name'], request.form['code_name'], request.form['phone_number'])

    return render_template('sisestamine_success.html', agent = agent)

@app.route('/otsing', methods = ['GET'])
def otsing():
    full_data = datastuff.get_all_data_from_table("agents")

    return render_template('otsing.html')

if __name__ == "__main__":
    app.run()