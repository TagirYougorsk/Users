from uuid import UUID
from User import User
from UserModels import ReadUserModel, RegisterUserModel, UpdateUserModel

class UserRepository:
    __users : list[User]
    
    def __init__(self):
        self.__users = []
        
    def add(self, reg_model : RegisterUserModel) -> None:
        user : User = User(reg_model.email, 
                        reg_model.password, 
                        reg_model.name,
                        reg_model.surname,
                        reg_model.birthdate,
                        reg_model.gender)
        self.__users.append(user)
    
    def read(self) -> list[ReadUserModel]:
        return [ReadUserModel(
                id = user.id,
                email = user.email,
                name = user.name,
                surname = user.surname,
                birthdate = user.birthdate,
                age = user.age,
                gender = user.gender)
            for user in self.__users]
    
    def read_by_id(self, id : UUID) -> ReadUserModel | None:
        for user in self.__users:
            if(user.id == id):
                return ReadUserModel(
                    id = user.id,
                    email = user.email,
                    name = user.name,
                    surname = user.surname,
                    birthdate = user.birthdate,
                    age = user.age,
                    gender = user.gender)
        raise Exception("Пользовтель не найден")
    
    def update(self, id : UUID, update_model : UpdateUserModel) -> None:
        for user in self.__users:
            if(user.id == id):
                if(update_model.email != None):
                    user.email = update_model.email 
                if(update_model.name != None):
                    user.name = update_model.name 
                if(update_model.surname != None):
                    user.surname = update_model.surname 
                if(update_model.birthdate != None):
                    user.birthdate = update_model.birthdate 
                if(update_model.password != None):
                    user.password = update_model.password
                if(update_model.gender != None):
                    user.gender = update_model.gender
        return None          
        
    def delete(self, id : UUID) -> None:
        for user in self.__users:
            if(user.id == id):
                self.__users.remove(user)
                return None
        raise Exception("Пользователь не найден")
    
    def age_sort_asceding(self) -> list[ReadUserModel]:
        buffer : list[ReadUserModel] = self.read()
        buffer.sort(key=lambda user: user.age)
        return buffer
    
    def age_sort_desceding(self) -> list[ReadUserModel]:
        buffer : list[ReadUserModel] = self.read()
        buffer.sort(key=lambda user: user.age, reverse=True)
        return buffer
    
    def name_sort_asceding(self) -> list[ReadUserModel]:
        buffer : list[ReadUserModel] = self.read()
        buffer.sort(key=lambda user: user.name)
        return buffer
    
    def name_sort_desceding(self) -> list[ReadUserModel]:
        buffer : list[ReadUserModel] = self.read()
        buffer.sort(key=lambda user: user.name, reverse=True)
        return buffer
    
    def get_gender_tags(self) -> list[str]:
        buffer : list[str] = []
        for user in self.__users:
            if(user.gender not in buffer):
                buffer.append(user.gender)
        return buffer
    
    def gender_filter(self, value : str) -> list[ReadUserModel]:
        if value.lower() not in ["мужской", "женский"]:
            raise Exception("Некорректный пол")
        # return [ReadUserModel(
        #             id = user.id,
        #             email = user.email,
        #             name = user.name,
        #             surname = user.surname,
        #             birthdate = user.birthdate,
        #             age = user.age,
        #             gender = user.gender)
        #         for user in self.__users if user.gender == value]
        buffer : list[ReadUserModel] = []
        for user in self.__users:
            if(user.gender.lower() == value.lower()):
                buffer.append(ReadUserModel(
                    id = user.id,
                    email = user.email,
                    name = user.name,
                    surname = user.surname,
                    birthdate = user.birthdate,
                    age = user.age,
                    gender = user.gender))
        return buffer
    
    def search(self, value : str) -> list[ReadUserModel]:
        buffer : list[ReadUserModel] = []
        for user in self.__users:
            if value.lower() in user.name.lower() or value.lower() in user.surname.lower() or value.lower() in user.email.lower():
                buffer.append(ReadUserModel(
                    id = user.id,
                    email = user.email,
                    name = user.name,
                    surname = user.surname,
                    birthdate = user.birthdate,
                    age = user.age,
                    gender = user.gender))
        return buffer