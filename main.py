
from fastapi import FastAPI
from validation import *
import database

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user_registration")
def user_registration(user: registration):
    user = user.dict()
    database.users.append(user)
    print(f"\n\n databse users: {database.users}")
    return user

@app.get("/get_bloodbank/{city_name}")
def read_item(city_name: str):
    
    for i in database.blood_banks:
        if i['city'] == city_name:
            return i
        
    return "Not Found"


