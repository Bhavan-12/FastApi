from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id": user_id}

@app.get("users")
def get_users(name):
    return {"name": name}

@app.post("/create-user")
def create_user(name:str, age:int):
    return {
        "name": name,
        "age": age
    }