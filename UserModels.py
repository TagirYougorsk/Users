from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr

class RegisterUserModel(BaseModel):
    email : EmailStr
    password : str
    name : str
    surname : str
    birthdate : datetime
    gender : str
    
class LoginUserModel(BaseModel):
    email : EmailStr
    password : str
    
class ReadUserModel(BaseModel):
    id : UUID
    email : EmailStr 
    name : str
    surname : str
    birthdate : datetime
    age : int
    gender : str
    
class UpdateUserModel(BaseModel):
    email : EmailStr | None
    name : str | None
    surname : str | None
    birthdate : datetime | None
    password : str | None
    gender : str | None
