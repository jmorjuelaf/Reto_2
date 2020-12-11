from db.user_db import UserInDB
from db.user_db import update_user, get_user, delete_user, create_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut, UserAuth
from models.transaction_models import TransactionIn, TransactionOut
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()
@api.get("/")
async def home():
    return {"message":"My TIC Finances"}

@api.post("/user/auth/")
async def auth_user(user_in: UserAuth):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/user/info/{username}")
async def get_info(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


@api.post("/user/create/")
async def make_create_user(user_in: UserIn):

    create_user(user_in)

    return {"El usuario ha sido creado": True}


@api.put("/user/update/")
async def make_update(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    update_user(user_in_db)

    return {"Actualizado": True}


@api.delete("/user/delete/")
async def make_delete_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    delete_user(user_in_db)

    return {"Eliminado": True}
