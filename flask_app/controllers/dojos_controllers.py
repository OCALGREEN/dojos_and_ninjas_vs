from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojo

# Home Page
@app.route("/")
def home():
    list_of_dojos = Dojo.get_all() # gets all the dojos and puts it in the variable
    return render_template("dojo.html", all_dojos = list_of_dojos) # creates a variable ready for html

@app.route("/update_dojo", methods=["POST"])
def update_dojo():
    Dojo.create(request.form)
    return redirect("/")