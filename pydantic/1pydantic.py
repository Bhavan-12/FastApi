from pydantic import BaseModel, Field, EmailStr, field_validator, computed_field
""""
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

class EmailStudent(BaseModel):
    name : str
    email : EmailStr

s = EmailStudent(name="bhavan", email="bhavanvadlani@gmail.com")
print(s)"""

class Student(BaseModel):
    id : int
    name: str = Field(..., min_length=2, max_length=20)
    age: int = Field(..., gt= 18, le=60)
    email: EmailStr
    course: str
    marks: int 

    @field_validator("name")
    @classmethod
    def checkname(cls, value: str) -> str:
        if not value.replace(" ","").isalpha():
            raise ValueError('name must contain letters and spaces only')
        return value.title()

    @computed_field
    @property
    def grade(self) -> str:
        if self.marks>90:
            return "O Grade"
        elif self.marks>80:
            return "A+ Grade"
        elif self.marks>70:
            return "A Grade"
        elif self.marks<35:
            return "Fail"

s = Student(
    id="10001", 
    name="bhavan",
    age="19", 
    email="bhavanvadlani@gmail.com", 
    course="python", 
    marks=90
)
print(s)


data = s.model_dump()
print(type(data))