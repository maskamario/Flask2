from flask import Flask, render_template, request, redirect
app = Flask(__name__)

lause = 'MARIE UNDER NIKKUS OBLIKATE VAHEL! ARTUR ATSON NIKKUS OBLIKATE VAHEL!'
nimekiri = lause.split(" ")
x= 0

@app.route('/', methods = ['POST', 'GET'])
def index():
    global x
    sisu = " "
    if request.method == 'POST':
        if x < len(nimekiri):
            sisu = nimekiri[x]
            x += 1
        else:
            x = 1
            sisu = nimekiri[0]

    return render_template('index.html', sisu = sisu)




if __name__ == "__main__":
    app.run()