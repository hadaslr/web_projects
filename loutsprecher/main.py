from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/2')
def x():
    return '''
    <html>
        <body>
            <div style="height: 100vh; width: 100vw; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;">
                <div style="background: red;"></div>
                <div style="background: blue; "></div>
                <div style="background: green;"></div>
                <div style="background: red;"></div>
            </div>
        </body>
    </html>'''

app.run(debug=True)