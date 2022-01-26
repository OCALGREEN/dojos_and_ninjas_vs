from tkinter.messagebox import RETRY
from unittest import result
from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.ate = data["ate"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, ate, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(ate)s, %(dojo_id)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return result

    # read one
    @classmethod
    def ninja_get_one(cls, data):
        query = "SELECT * FROM dojos_and_ninjas.ninjas WHERE id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return cls(result[0])

    # read all
    @classmethod
    def ninja_get_all(cls, data):
        query = "SELECT * FROM dojos_and_ninjas.ninjas;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query)
        ninjas = []
        for row in result:
            ninjas.append(cls(row))
        return ninjas