import json
from typing import List
from app.schema import UserIn

def add_userdata(user_data: dict):
    try:
        with open('data/users.json', 'r+') as file:
            data = json.load(file)
            data.append(user_data)
            file.seek(0)
            json.dump(data, file)
    except FileNotFoundError:
        with open('data/users.json', 'w') as file:
            json.dump([user_data], file)

def read_usersdata() -> List[dict]:
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

