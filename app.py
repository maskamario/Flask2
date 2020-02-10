from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi_maska():
    return "Hi Maska, I'm alive"

if __name__ == "__main__":
    app.run()