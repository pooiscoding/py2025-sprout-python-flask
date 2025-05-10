from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/hello2")
def hello2():
    return "<h1>Hello2</h1>"

@app.route("/hello/<var1>")
def hello_name(var1):
    return f"<h1>Hello, {var1}</h1>"

if __name__ == "__main__":
    app.run()