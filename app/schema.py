from pydantic import BaseModel
from typing import List

class UserIn(BaseModel):
    name: str
    email: str

class BaseResponse(BaseModel):
    success: bool

class UserListOut(BaseModel):
    users: List[UserIn]

