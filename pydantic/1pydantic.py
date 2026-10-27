from pydantic import BaseModel

class simplestudent(BaseModel):
    name: str
    age: int
    marks: int

s = simplestudent(name = 'aarav', age = 20, marks = 100)
print(s)