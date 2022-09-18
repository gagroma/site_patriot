from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def siteyes():
    return render_template("sityes.html")

class Main():
    def __init__(self):
        print("init")