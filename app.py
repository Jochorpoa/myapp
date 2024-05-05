from flask import Flask, render_template, request, flash

app=Flask(__name__)
app.secret_key= "jochorpoa06"

@app.route("/home")
def index():
    flash("What's your full name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['input_name']) + ", great to see you")
    return render_template("index.html")
