from fastapi import APIRouter

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)

@router.get("/")

def blog():
    return {"message": "Here are all blogs."}

