from uuid import UUID
from fastapi import FastAPI
import uvicorn
from InitData import init_data
from User import User
from UserModels import RegisterUserModel, UpdateUserModel
from fastapi.middleware.cors import CORSMiddleware
from UserRepository import UserRepository

user_repo = UserRepository()

init_data(user_repo)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def get_users():
    return user_repo.read()

@app.get("/users/{id}")
def get_user(id : UUID):
    try:
        return user_repo.read_by_id(id)
    except Exception as e:
        return str(e)

@app.post("/users")
def create_user(reg_model : RegisterUserModel):
    try:
        user_repo.add(reg_model)
        return "Пользователь успешно создан"
    except Exception as e:
        return str(e)

@app.put("/users/{id}")
def update_user(id : UUID, update_model : UpdateUserModel):
    try:
        user_repo.update(id, update_model)
        return "Пользователь успешно обновлен"
    except Exception as e:
        return e     

@app.delete("/users/{id}")  
def delete_user(id : UUID):
    try:
        user_repo.delete(id)
        return "Пользователь успешно удален"
    except Exception as e:
        return str(e)

@app.get("/age_sort_asceding")
def age_sort_asceding():
    return user_repo.age_sort_asceding()

@app.get("/age_sort_desceding")
def age_sort_desceding():
    return user_repo.age_sort_desceding()

@app.get("/name_sort_asceding")
def name_sort_asceding():
    return user_repo.name_sort_asceding()

@app.get("/name_sort_desceding")
def name_sort_desceding():
    return user_repo.name_sort_desceding()

@app.get("/get_gender_tags")
def get_gender_tags():
    return user_repo.get_gender_tags()

@app.get("/get_gender_filter/{value}")
def get_gender_filter(value : str):
    try:
        return user_repo.gender_filter(value)
    except Exception as e:
        return str(e)

@app.get("/search/{value}")
def search(value : str):
    return user_repo.search(value)

uvicorn.run(app)