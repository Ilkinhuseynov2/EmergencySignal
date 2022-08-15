import email
from typing import Union
from fastapi import FastAPI, Depends
from .schema import User 
from .database import Base, engine, SessionLocal
from .crud import create_users
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World."}


@app.post("/user")
def create_user(user: User, db: Session = Depends(get_db)):
    create_users(db = db, user = user)
    return {"username":  user.username, "email": user.email, "password": user.password}