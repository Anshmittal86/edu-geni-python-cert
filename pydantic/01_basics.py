from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    age: int
    

user = {
    'id': 10,
    'username': 'Aman',
    'age': 20
}

user = User(**user)

print(User)