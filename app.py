from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:omran@localhost/mydb'
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route("/")
def index():
    return render_template("index.html")


