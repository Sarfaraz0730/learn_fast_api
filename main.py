from fastapi import FastAPI
from fastapi.params import Query
from routers import user, blog, order, product

app = FastAPI()

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(order.router)
app.include_router(product.router)
@app.get("/greet")
def greet_user(name: str = Query(..., title="Name of the user"), message: str = Query(..., title="Custom greeting message")):
    return {"message": f"{message}, {name}!"}
