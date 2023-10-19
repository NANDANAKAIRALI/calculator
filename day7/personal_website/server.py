from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def guess():
    return render_template("spotify.html")