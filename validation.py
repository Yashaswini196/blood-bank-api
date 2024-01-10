from pydantic import BaseModel

class registration(BaseModel):
    name: str
    email: str
    password: str

