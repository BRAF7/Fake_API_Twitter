#Pydantic
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
#Python
#Helps creating ID´s
from uuid import UUID
from typing import Optional
from datetime import date
from datetime import datetime

class UserBase(BaseModel):
    user_id: UUID  = Field(...)
    email : EmailStr = Field(...)




class PasswordBase(BaseModel):
    password : str = Field(
        ...,
        min_length = 8,
        max_length = 64,
        example='12345678'
    )

class UserLogin(UserBase, PasswordBase):
    pass

class User(UserBase):
    first_name : str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example= 'Mar'
    )
    
    last_name : str  = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example='Pascacio'
    )
    birth_date : Optional[date] = Field(default=None)




class UserRegister(User,PasswordBase):
    pass




class Tweet(BaseModel):
    tweet_id : UUID = Field(...)
    content : str = Field(
        ...,
        min_length=1,
        max_length=256,
        example = 'Hello I´m tweet'
    )
    created_at : datetime = Field(default= datetime.now())
    updated_at : Optional[datetime] = Field(defaul=None)
    by : User = Field(...)