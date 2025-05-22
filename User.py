from datetime import datetime
import re
from uuid import UUID
import uuid
from pydantic import EmailStr
from dateutil.relativedelta import relativedelta

class User:
    __id : UUID
    email : EmailStr 
    __password : str
    __name : str
    __surname : str
    __birthdate : datetime
    __gender : str
    
    def __init__(self, email : EmailStr, password: str, name: str, surname : str, birthdate : datetime, gender : str):
        self.__id = uuid.uuid4()
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    @property
    def id(self):
        return self.__id
    
    @property
    def age(self):
        return int((datetime.now() - self.birthdate).days / 365.2425)
    
    @property
    def password(self):
        return self.__password 
    @password.setter
    def password(self, value : str):
        if(not(8 < len(value) < 20)):
            raise Exception("Длина пароля должна быть от 8 до 20 символов")
        if(not bool(re.search(r'[A-Z]', value))):
            raise Exception("Пароль должен содержать хотя-бы одну заглавную букву")
        if(not bool(re.search(r'[a-z]', value))):
            raise Exception("Пароль должен содержать хотя-бы одну прописную букву")
        if(not bool(re.search(r'\d', value))):
            raise Exception("Пароль должен содержать хотя-бы одну прописную букву")
        self.__password = value
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value : str):
        self.__name = value
        
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, value : str):
        self.__surname = value
   
    @property
    def birthdate(self):
        return self.__birthdate
    @birthdate.setter
    def birthdate(self, value : datetime):
        if(value > (datetime.now() - relativedelta(years = 18))):
            raise Exception("Вам должно быть больше 18 лет")
        self.__birthdate = value

    @property
    def gender(self): 
        return self.__gender
    @gender.setter
    def gender(self, value : str):
        if(value.lower() not in ["мужской", "женский"]):
            raise Exception("Пола всего два")
        self.__gender = value  