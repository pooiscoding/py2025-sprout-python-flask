from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

REDIRECT_URL = "https://www.youtube.com/watch?v=cJnO-Y_YnFg"

@app.route("/redirect")
def redirect_to_yt():
    return redirect(REDIRECT_URL)

if __name__ == "__main__":
    app.run()