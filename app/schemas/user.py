from pydantic import BaseModel, ConfigDict, EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
