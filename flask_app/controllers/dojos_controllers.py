from flask import render_template, redirect, session, request
from markupsafe import re
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def home():
    return render_template("dojo.html", all_dojos = Dojo.get_all()) # creates a variable ready for html

@app.route("/update_dojo", methods=["POST"]) # will create a new dojo and redirect to the home page
def update_dojo():
    Dojo.create(request.form)
    return redirect("/")

@app.route("/show/dojo/<int:dojo_id>/ninja")
def show_dojo_ninja(dojo_id):
    return render_template("showdojo.html", this_dojo = Dojo.get_one({"id": dojo_id}))

@app.route("/dojo/<int:id>")
def show_dojo(id):
    data = {"id": id}
    return render_template("showdojo.html", dojo = Dojo.get_one_with_ninjas(data))