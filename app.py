from flask import Flask, render_template, url_for, request
import pandas as pd

app = Flask(__name__)
       
@app.route("/")
def homepage():  
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
