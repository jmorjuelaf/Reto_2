from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    dob: str

class UserOut(BaseModel):
    username: str
    email: str
    dob:str


class UserAuth(BaseModel):
    username: str
    password: str


