from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojo

# Home Page
@app.route("/")
def home():
    return render_template("dojo.html")

@app.route("/update_dojo", methods=["POST"])
def update_dojo():
    Dojo.create(request.form)
    return redirect("/")