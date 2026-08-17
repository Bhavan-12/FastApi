from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "this is home page"}

@app.get("/about")
def about():
    return {"message": "this is about page"}

@app.get("/users")
def users():
    return {
        "users" : ["bhavan", "student", "spiderman", "batman"]
    }
