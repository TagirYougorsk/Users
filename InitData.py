from datetime import datetime
from UserModels import RegisterUserModel
from UserRepository import UserRepository


def init_data(user_repo : UserRepository):
    #region init_data
    user_repo.add(RegisterUserModel( 
        email="harasow@mail.ru", 
        password="Q123w123_!", 
        name="Tagir", 
        surname="Kharasov",
        birthdate=datetime(1984,6,8),
        gender="Мужской"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="ЯЯЯЯЯЯЯ", 
        surname="Первый",
        birthdate=datetime(1899,3,4),
        gender="Мужской"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="ГГГГГГГ", 
        surname="Первый",
        birthdate=datetime(1989,3,4),
        gender="Мужской"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="ЖЖЖЖЖЖЖ", 
        surname="Первый",
        birthdate=datetime(1779,3,4),
        gender="Мужской"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="ВВВВВВВВ", 
        surname="Первый",
        birthdate=datetime(1777,3,4),
        gender="Женский"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="ЛЛЛЛЛЛЛЛЛ", 
        surname="Первый",
        birthdate=datetime(2005,3,4),
        gender="Женский"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="МММММММММ", 
        surname="Первый",
        birthdate=datetime(2001,3,4),
        gender="Женский"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="НННННННННН", 
        surname="Первый",
        birthdate=datetime(2002,3,4),
        gender="Женский"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="КККККККК", 
        surname="Первый",
        birthdate=datetime(2003,3,4),
        gender="Женский"))

    user_repo.add(RegisterUserModel( 
        email="123@mail.ru", 
        password="123aaaAAA", 
        name="ААААААААА", 
        surname="Первый",
        birthdate=datetime(2003,3,4),
        gender="Женский"))
    
    
   
    #endregion`