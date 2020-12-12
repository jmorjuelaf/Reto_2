from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    email: str
    dob: str

database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "email":"camilo24@latinmail.com",
                            "dob":"1999-12-07"}),

    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "email": "andres18@latinmail.com",
                            "dob": "1995-10-07"}),
    "santi2020": UserInDB(**{"username": "santi2020",
                             "password": "caliescali",
                             "email": "santi_20@uk.co",
                             "dob": "1991-08-20"}),
    "dinho10": UserInDB(**{"username": "dinho10",
                           "password": "samba",
                           "email": "barsa_r10@aol.es",
                           "dob": "1989-12-06"}),
    "OAMR04": UserInDB(**{"username": "OAMR04",
                          "password": "lacalle",
                          "email": "OM@gmail.com",
                          "dob": "2000-06-22"}),
    "szapatao": UserInDB(**{"username": "szapatao",
                            "password": "suamadre",
                            "email": "szapatao@unal.edu.co",
                            "dob": "1992-04-07"}),
    "JuanEs05": UserInDB(**{"username": "JuanEs05",
                            "password": "naruto",
                            "email": "juanes@gmail.com",
                            "dob": "1995-06-13"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db

def create_user(user_in_db: UserInDB):

    database_users[user_in_db.username] = user_in_db

def delete_user(user_in_db: UserInDB):
    del database_users[user_in_db.username]

