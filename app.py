from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/hola/')
def hola():
     return render_template("hola.html")