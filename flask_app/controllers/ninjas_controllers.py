from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route("/ninjas")
def ninjas():
    return render_template("addninja.html", dojos = dojo.Dojo.get_all()) # dojos variable = dojo(file).Dojo(class).get_all(get all function in the class)

@app.route("/create/ninja", methods=["POST"])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect("/")