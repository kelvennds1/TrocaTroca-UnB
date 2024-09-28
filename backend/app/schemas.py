
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints, field_validator
from typing import Optional

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserCreate(BaseModel):
    registration: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    password_hash: Annotated[str, StringConstraints(min_length=8, max_length=1000)]
    name: Annotated[str, StringConstraints(min_length=1, max_length=255)]
    user_name: Annotated[str, StringConstraints(min_length=1, max_length=255)]
    email: EmailStr
    profile_picture: Optional[bytes] = None  # foto de perfil opcional

    @field_validator('email')
    def validate_email(cls, v):
        if not v.endswith('@aluno.unb.br'):
            raise ValueError('Email must be @aluno.unb.br')
        return v

class UserRead(BaseModel):
    id: int
    registration: str
    name: str
    user_name: str
    email: str

    class Config:
        from_attributes = True

# Category Schemas
class CategoryCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=255)]
    description: Optional[Annotated[str, StringConstraints(max_length=500)]] = None

class CategoryRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True

# Item Schemas
class ItemCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=255)]
    image: Optional[bytes] = None
    model: Optional[Annotated[str, StringConstraints(max_length=100)]] = None
    brand: Optional[Annotated[str, StringConstraints(max_length=100)]] = None
    year_acquired: Optional[Annotated[str, StringConstraints(max_length=45)]] = None
    description: Optional[Annotated[str, StringConstraints(max_length=1000)]] = None
    condition: Optional[Annotated[str, StringConstraints(max_length=100)]] = None
    vaccines: Optional[Annotated[str, StringConstraints(max_length=500)]] = None
    likes: Optional[Annotated[str, StringConstraints(max_length=500)]] = None
    dislikes: Optional[Annotated[str, StringConstraints(max_length=500)]] = None
    item_type: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    category_id: int
    owner_id: int

class ItemRead(BaseModel):
    id: int
    name: str
    model: Optional[str] = None
    brand: Optional[str] = None
    year_acquired: Optional[str] = None
    description: Optional[str] = None
    condition: Optional[str] = None
    vaccines: Optional[str] = None
    likes: Optional[str] = None
    dislikes: Optional[str] = None
    item_type: str

    class Config:
        from_attributes = True

# Swap Schemas
class SwapCreate(BaseModel):
    initiator_id: int
    receiver_id: int
    item_offered_id: int
    item_requested_id: int
    status: Optional[Annotated[str, StringConstraints(max_length=50)]] = 'pending'

class SwapRead(BaseModel):
    id: int
    initiator_id: int
    receiver_id: int
    item_offered_id: int
    item_requested_id: int
    status: str

    class Config:
        from_attributes = True
