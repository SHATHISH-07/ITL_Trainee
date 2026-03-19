from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

users_list = []

@app.get("/")
def read_root():
    return {"message":"Hello from Fast API"}

@app.get("/users")
def get_all_user():
    return {
        "users":users_list
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/items/")
def get_items(limit : int = 10):
    return {"limit":limit}

@app.post("/users/")
def create_user(user:User):
    users_list.append(user)
    return {
        "user":user
    }

