import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from .ninja import Ninja 

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return result

    # read one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return cls(result[0])

    # read all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []
        for row in result:
            dojos.append(cls(row))
        return dojos 

    # associate many to one
    @classmethod
    def get_one_with_ninjas(cls, data): 
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        dojo = cls(result[0])
        for row_from_db in result:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["ninjas.first_name"],
                "last_name": row_from_db["ninjas.last_name"],
                "ate": row_from_db["ninjas.ate"],
                "created_at": row_from_db["ninjas.created"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo 