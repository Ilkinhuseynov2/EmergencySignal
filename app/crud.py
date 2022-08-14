from sqlalchemy.orm import Session

from . import models



def create_user(db: Session, username: username, email: email, password: password):
    fake_hashed_password = password + "notreallyhashed"
    db_user = models.User(username = username, email=email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
