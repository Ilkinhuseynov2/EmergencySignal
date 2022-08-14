from sqlalchemy.orm import Session
from .schema import User

from . import models



def create_users(db: Session, user: User):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username = user.username, email=user.email, password=fake_hashed_password, phone = user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
