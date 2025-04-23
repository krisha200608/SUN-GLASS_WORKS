from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/intake")
def intake():
    return render_template("intake.html")  # use correct folder path


app.run(host='0.0.0.0', debug=True)
    