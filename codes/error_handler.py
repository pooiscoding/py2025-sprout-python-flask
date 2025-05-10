from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

GIF_URL = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNuMHg4djM4M3NsY29obDNwc3lrcDc2dmZzN3pqZ3IyeDU2Mmo0NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uFygSquQkzbJTn3eQe/giphy.gif"

@app.errorhandler(404)
def not_found_error(e):
    return f"<img src=\"{GIF_URL}\" alt=\"not found\"/>", 404

@app.route("/notfound")
def raise_not_found():
    abort(404)

if __name__ == "__main__":
    app.run()