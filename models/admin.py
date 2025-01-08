from pydantic import BaseModel

class Admin(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
