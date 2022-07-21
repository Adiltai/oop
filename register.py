import json


FILE='jsondb/users.json'

def validate_password(password):
    if len(password)<8:
        raise Exception('Пароль слишком короткий!')
    elif password.isdigit() or password.isalpha():
        raise Exception('Пароль должен состоять из букв и цифр!')

class RegisterMixin:
    """    Миксин для регистрации юзера    """
    def register(self, username, password):
        validate_password(password)

        with open(FILE, 'r') as file:
            try:
                data=json.load(file)
                data[-1]['id']+1
            except:
                id=1
                data=[]

        with open(FILE, 'w') as file:
            if data:
                is_exists_username= any([x['username']== username for x in data])
                if is_exists_username:
                    json.dump(data, file)
                    raise Exception("Такой юсер уже есть!")
            else:
                data.append({'id':id, 'username':username, 'password':password})
                json.dump(data, file)
                return 'successfully registerd'

class LoginMixin:
    """    Миксин для login   """
    def login(self, username, password):
        with open (FILE, 'r') as file:
            data= json.load(file)
            is_registered = any([x['username']==username for x in data])
            if not is_registered:
                raise Exception('Нет такого username!')

            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            if user_data['password'] != password:
                raise Exception('Неверный пароль')
            return {'msg': 'Successfully loged in', 'user':user_data}

class User(RegisterMixin, LoginMixin):
    pass
# with open (FILE, 'w'):
#     pass

# user = User()
# print(user.register('JohnSnow', 'john1234')) 
# print(user.login('JohnSnow','john1234'))






