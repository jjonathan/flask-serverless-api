# app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/new-route")
def newroute():
    return "meu new route!"s