from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    name: str
    email: str
    password: str  # Include password for user creation

# Add this schema for read operations
class UserRead(BaseModel):
    id: int
    name: str
    email: str
