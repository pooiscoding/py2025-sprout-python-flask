from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/login")
def login():
    pwd = request.args.get("password")
    if pwd == "haha":
        return "<h1>Correct</h1>"
    else:
        return "<h1>Forbidden</h1>", 403

if __name__ == "__main__":
    app.run()