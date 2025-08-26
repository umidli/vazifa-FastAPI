from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = [
    {"id": 1, "name": "Ali", "address": "Toshkent"},
    {"id": 2, "name": "Vali", "address": "Samarqand"},
    {"id": 3, "name": "Salim", "address": "Buxoro"},
    {"id": 4, "name": "Karim", "address": "Andijon"},
    {"id": 5, "name": "Aziz", "address": "Namangan"}
]


@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    
app.get("/users/address/{address}")
def by_address(address: str):
    result = [user for user in users if user["address"].lower() == address.lower()]
    if result:
        return result
    
@app.post("/users")
def add_user(user: dict):
    users.append(user)
    return {"message": "user muvafaqiyatli tarzda qo'shildi", "user": user}

    


if __name__ == '__main__':
    uvicorn.run(app)

