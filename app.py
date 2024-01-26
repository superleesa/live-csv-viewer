from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("data.csv")
    html = df.to_html()
    return render_template("table.html", html=html)