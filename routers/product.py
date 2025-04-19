from fastapi import APIRouter, Response, status
from pydantic import BaseModel, Field, EmailStr

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

@router.get("/")

def product():
    return {"message": "This is user info."}



class productSchema(BaseModel):
    name:str
    price:int =10
    in_stock: bool
    category: str


@router.post("/add-product")

def products(prod:productSchema):

    
     
    return {
        f"message {prod}"
    }

