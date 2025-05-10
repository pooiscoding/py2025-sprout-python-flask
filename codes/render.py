from flask import Flask, render_template

app = Flask(__name__)

"""
params = {
    "header" : "標題",
    "n1" : 1,
    "n2" : 2,
    "n3" : 3,
    "n4" : 4
}
params = {
    "header" : "標題",
    "n1" : 5,
    "n2" : 2,
    "n3" : 3,
    "n4" : 7
}
"""

@app.route("/")
def hello():
    params = {
        "header" : "標題",
        "n1" : 5,
        "n2" : 2,
        "n3" : 3,
        "n4" : 7
    }
    return render_template("index.html", **params)

if __name__ == "__main__":
    app.run()