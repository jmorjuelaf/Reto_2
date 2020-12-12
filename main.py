from db.user_db import UserInDB
from db.user_db import update_user, get_user, delete_user, create_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut, UserAuth
from models.transaction_models import TransactionIn, TransactionOut
import datetime
from fastapi import FastAPI, HTTPException
from string import digits

api = FastAPI()
@api.get("/")
async def home():
    return {"message":"My TIC Finances"}

# @api.post("/user/auth/")
# async def auth_user(user_in: UserAuth):

#     user_in_db = get_user(user_in.username)

#     if user_in_db == None:
#         raise HTTPException(status_code=404, detail="El usuario no existe")

#     if user_in_db.password != user_in.password:
#         return  {"Autenticado": False}

#     return  {"Autenticado El usuario " + user_in.username + " ha ingresado" }


@api.post("/user/auth/")
async def auth_user(username: str,password: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != password:
        return  {"Acceso denegado, Credenciales incorrectas"}

    return  {"Autenticado El usuario " + username + " ha ingresado" }


@api.get("/user/info/")
async def get_info(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


# @api.post("/user/create/")
# async def make_create_user(user_in: UserIn):


#     if user_in.username == "" or user_in.password == "" or user_in.email == "" or user_in.dob == "":
#         return "Información incompleta para crear usuario"
#     else:   
#         create_user(user_in)
#         return {user_in.username + " ha sido creado"}

#     #return {"El usuario ha sido creado": True}
#     return {user_in.username + " ha sido creado"}
# {username}/{password}/{email}/{dob}

@api.post("/user/create/")
async def make_create_user(username: str,password: str,email: str,dob: str):


    if username == "" or password == "" or email == "" or dob == "":
        return "Información incompleta para crear usuario"
    else:   
        
        # info = dict({"username":username, "password":password, "email":email, "dob":dob})
     
        user_in = UserIn(**dict({"username":username, "password":password, "email":email, "dob":dob}))
        create_user(user_in)

        return {username + " ha sido creado"}

    #return {"El usuario ha sido creado": True}
    return {username + " ha sido creado"}


@api.put("/user/update/")
async def make_update(username: str,password: str,email: str,dob: str):

    user_in_db = get_user(username)



    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        user_in_db = UserIn(**dict({"username":username, "password":password, "email":email, "dob":dob}))
        update_user(user_in_db)
        return {"El usuario " + username + " ha sido actualizado"}

    return None


# @api.delete("/user/delete/")
# async def make_delete_user(user_in: UserIn):

#     user_in_db = get_user(user_in.username)

#     if user_in_db == None:
#         raise HTTPException(status_code=404, detail="El usuario no existe")

#     delete_user(user_in_db)

#     return {"Eliminado": True}

@api.delete("/user/delete/")
async def make_delete_user(username):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    delete_user(user_in_db)

    return {"El usuario " + username + " ha sido eliminado"}


