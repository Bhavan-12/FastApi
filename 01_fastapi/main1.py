from fastapi import FastAPI, HTTPException
import json

app= FastAPI()

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

def get_students():
    with open("students.json", "r") as file:
            return json.load(file)
    
@app.get("/students")
def students():
    return get_students()

@app.get("/student/{student_id}")
def get_id(student_id:str):
    data = get_students()
    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail= f"student with id '{student_id}' does not exist")
        return data[student_id]

@app.get("/filter")
def filter(course:str = None):
    data = get_students()
    if course is None:
        return data 
    filtered = {}
    for student_id, info in data.items():
        if info["course"].lower()== course.lower():
            filtered[student_id] = info
    return filtered

@app.get("/sort")
def sort( )