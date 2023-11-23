from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main_menu.html")


@app.route("/levels")
def levels():
    return render_template("levels.html")


@app.route("/dlc")
def dlc():
    return render_template("dlc.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


app.run(debug=True)
