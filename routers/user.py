from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/info")

def user_function():
    return {"message": "This is user info."}


@router.post("/")

def create_user():

    return "user is created"

