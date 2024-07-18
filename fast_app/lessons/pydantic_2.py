from pydantic import BaseModel, Field
from typing import Optional as optional


class P(BaseModel):
    name: str
    age: int | None = Field(default=123, ge=5)
    email: str
    password: str


# d = {"name": "test_name", "age": 20, "email": "name@test.gr", "password": "123456789"}
p = P(name="test_name", email="name@test.gr", password="123456789")
# p = P(**d)
print(p)
