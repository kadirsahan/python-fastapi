from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel,ValidationError
from datetime import datetime

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)

print(user.id)

app = FastAPI()

@app.get("/ksk")
async def ksk():
    return "kaf sin kaf"

print(user.dict())

external_data = {
    'id': 'ksk',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

try:
    user = User(**external_data)
except ValidationError as e:
    print(e.json())

@app.get("/team/{name}")
async def hello(name):
    return f"en buyuk {name}"