from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def banana():
    return render_template("main_menu.html")


@app.route("/levels")
def banana1():
    return render_template("levels.html")


@app.route("/dlc")
def banana2():
    return render_template("dlc.html")


@app.route("/settings")
def banana3():
    return render_template("settings.html")


app.run(debug=True)
