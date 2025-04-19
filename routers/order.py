from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix="/order",
    tags=["order"]
)

@router.get("/info")

def order_function():
    return {"message": "Order 123 created."}

