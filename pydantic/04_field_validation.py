from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        description='Employee Name', 
        examples='John Doe'
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10_000, # gt (grater than), ge(greater than and equal to)
        le=10_000_00, # lt (less than), le(less than and equal to)
        description='Annual Salary in USD.'
    )
    
employee = Employee(
    id=1,
    name="John Doe",
    department='Security',
    salary=14_000
)

print(employee)