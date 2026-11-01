from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator, Field, computed_field, EmailStr
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

def save_data():
    with open("students.json", "w") as file:
        
    
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

@app.get("/paginate")
def paginate_students(page:int, limit:int):
    data = get_students()
    students = []
    for student_id, info in data.items():
        info['id'] = student_id
        students.append(info)
    start = (page-1) * limit
    end = start + limit
    page_student = students[start:end]
    total_students = len(students)

    return {
        "page": page,
        "limit": limit,
        "total_students": total_students,
        "students": page_student
    }

class Student(BaseModel):
    id: int  # Keeps it as an integer internally
    name: str = Field(..., min_length=2, max_length=20)
    age: int = Field(..., gt=18, le=60)
    email: EmailStr
    course: str
    marks: int 

    @field_validator("name")
    @classmethod
    def checkname(cls, value: str) -> str:
        if not value.replace(" ", "").isalpha():
            raise ValueError('name must contain letters and spaces only')
        return value.title()

    @computed_field
    @property
    def grade(self) -> str:
        # Added '>=' to cover exact edge marks like 90, 80, 70
        if self.marks >= 90:
            return "O Grade"
        elif self.marks >= 80:
            return "A+ Grade"
        elif self.marks >= 70:
            return "A Grade"
        elif self.marks < 35:
            return "Fail"
        else:
            return "B Grade"  # Fallback safety net for marks between 35 and 69

with open("students.json", "r") as file:
    raw = json.load(file)

for student_id, info in raw.items():
    # Fix: Extract only the numbers from 'S001' to turn it into an integer 1
    numeric_id = int(''.join(char for char in student_id if char.isdigit()))    
    s = Student(id=numeric_id, **info)


@app.post("/create", status_code=201)
def create_student(student: Student):
    data = get_students()

    data[Student.id] = Student.model_dump(exclude={"id"})
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)
