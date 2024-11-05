from typing import List
from fastapi import FastAPI
import json

from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()
router = APIRouter()

@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Hello from FastAPI ;)"}

@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    """
    Add user data to json file
    """
    try:
        services.add_userdata(user.dict())
    except:
        return {"success": False}
    return {"success": True}

@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from json file
    """
    return services.read_usersdata()

@router.get("/users", response_model=UserListOut)
async def get_users():
    try:
        with open("data/users.json", "r") as f:
            users = json.load(f)
        # Ensure the returned data matches the expected structure
        return {"users": users}  # Wrap users list in a dictionary with 'users' key
    except Exception as e:
        return {"error": str(e)}

