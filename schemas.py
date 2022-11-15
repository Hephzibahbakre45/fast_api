from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"Popsicool",
                "email":"akinolasamson1234@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = "97adab5442a1b7954f265acb58f25867f54bd7275645df3b5efa0b6fbced9b71"


    

class LoginModel(BaseModel):
    username:str
    password:str

    

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]

    class Config:
        arbitrary_types_allowed = True
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE",
            }
        }

class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode = True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }