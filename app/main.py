from typing import Union
from fastapi import FastAPI
from .database import SessionLocal, engine
from . import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World."}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id + 12, "q": q}

@app.get("/user/{username}/{email}/{password}")
def create_user(username: str, email: str, password: str):
    return {"username":  username, "email": email, "password":password}