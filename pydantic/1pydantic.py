from pydantic import BaseModel, Field

class simplestudent(BaseModel):
    name: str
    age: int
    marks: int

s = simplestudent(name = 'aarav', age = 20, marks = 100)
print(s)

class RuleStudent(BaseModel):
    name : str = Field(..., min_length = 2, max_length = 50)
    age : int = Field(..., min=18, max=65)
    marks : int =Field(..., min=35, max = 100)

s = RuleStudent(name = "bhavan", age = 16, marks=77)
print(s)