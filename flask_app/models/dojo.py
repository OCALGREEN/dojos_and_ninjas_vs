import imp
from unittest import result
from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos_and_ninjas.dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return result
    # read one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos_and_ninjas.dojos WHERE id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return cls(result[0])
    # read all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos_and_ninjas.dojos;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []
        for row in result:
            dojos.append(cls(row))
        return dojos 