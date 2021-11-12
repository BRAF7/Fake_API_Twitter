#Pydantic
from pydantic import BaseModel, Field

#FastAPI
from fastapi import FastAPI
from pydantic.networks import EmailStr
#Python
#Helps creating ID´s
from uuid import UUID
from typing import Optional
from datetime import date

#we defined our app
app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID  = Field(...)
    email : EmailStr = Field(...)

class UserLogin(UserBase):
    password : str = Field(
        ...,
        min_length = 8,
        max_length = 64,
    )

class User(UserBase):
    first_name : str = Field(
        ...,
        min_length = 1,
        max_length = 50,
    )
    
    last_name : str  = Field(
        ...,
        min_length = 1,
        max_length = 50,
    )
    birth_date : Optional(date) = Field(default=None)

class Tweet(BaseModel):
    pass

@app.get(path='/')
def home() -> dict:
    return {'Twiterr' : 'con FastAPI'}