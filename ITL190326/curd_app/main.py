from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models,schemas
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    print("4. Home endpoint hit!")
    return {"message":"you can Start"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create new user
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.Users(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Read all user
@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

# Read one user
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id:int, db: Session = Depends(get_db)):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

# Update a User
@app.put("/user/{user_id}")
def update_user(user_id:int, user:schemas.UserCreate,db: Session = Depends(get_db)):
    existing_user = db.query(models.Users).filter(models.Users.id == user_id).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    existing_user.name = user.name
    existing_user.age = user.age

    db.commit()
    db.refresh(existing_user)
    return {"message":"User updated"}

# Delete a User
@app.delete("/user/{user_id}")
def delete_user(user_id:int, db: Session = Depends(get_db)):
    existing_user = db.query(models.Users).filter(models.Users.id == user_id).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(existing_user)
    db.commit()

    return {"message":"User Deleted"}