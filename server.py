from flask_app import app
from flask_app.controllers import dojos_controllers, ninjas_controllers

if __name__ == "__main__":
    app.run(debug=True)