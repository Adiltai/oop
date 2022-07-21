# Принципы в ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиция
# 6. Агрегация

# Наследование - позволяет принимать методы, атрибуты и поведение

# Родительский класс
# Дочерний класс

# class Animal:
#     def say(self):
#         print("I'm animal!")
# class Croco(Animal):
#     pass
# croco = Croco()
# croco.say()
# croco = Animal()
# croco.say()

#-----------------------------------------------------------------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary
#     def get_fullName(self):
#         return f'{self.name} {self.last_name}'
#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# emp1 = Employee('John', 'Snow', 2000)
# print(emp1.get_fullName())
# print(emp1.salary)
# emp1.give_bonus()
# print(emp1.salary)

#-----------------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'Меня зовут {self.name}, мне {self.age} лет.')
# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer
#     def info(self):
#         super().info()
#         print(f'Я учусь в университете {self.univer}')
# talgat = Student('Talgat', 17, 'MIT')
# talgat.info()
# print(talgat.name)

#------------------------------------------------------------------------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary
#     def get_fullName(self):
#         return f'{self.name} {self.last_name}'
#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_lang):
#         super().__init__(name, last_name, salary)
#         self.lang = prog_lang
# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps = None):
#         super().__init__(name, last_name, salary)
#         if emps == None:
#             self.emps = []
#         else:
#             self.emps = emps
#     def add_emp(self, emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#         else:
#             print('Employee already is in!')
#     def show_emps(self):
#         result = []
#         for emp in self.emps: 
#             result.append(emp.get_fullName())
#         return result

# dev1 = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Steve', 'Wozniak', 2000, 'JS')
# dev3 = Developer('Larry', 'Page', 1000, 'JS')
# dev4 = Developer('Jamie', 'Lannister', 1500, 'Python')

# manager1 = Manager('Ivan', 'Ivanov', 3000, emps = [dev2, dev3])
# manager2 = Manager('Aibek', 'Velikiy', 1500)

# manager2.add_emp(dev1)
# manager2.add_emp(dev4)

# print(manager1.show_emps())
# print(manager2.show_emps())

# print(f'Manager {manager1.get_fullName()}, has {manager1.show_emps()} developers. His salary is {manager1.salary}')
# manager2.give_bonus()
# print(f'Manager {manager2.get_fullName()}, has {manager2.show_emps()} developers. His salary is {manager2.salary}')

#--------------------------------------------------------------------------------------------------------------------------

# class Post:
#     def __init__(self, user):
#         self.user = user
#         self.posts = []
#         self.id = 0
#     #CRUD
#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id = self.id, title = title, body = body, image = image)
#         self.posts.append(post)
#         return {'status' : 201, 'msg' : 'Successfully created!'}
#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return post
#         return {'status' : 404, 'msg' : 'Not found!'}
#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 post.update(kwargs)
#                 return {'status' : 200, 'msg' : 'Updated'}
#         return {'status' : 404, 'msg' : 'Not found!'}
#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 index_post = self.posts.index(post)
#                 self.posts.pop(index_post)
#                 return {'status' : 204, 'msg' : 'No content, deleted!'}
#         return {'status' : 404, 'msg' : 'Not found!'}

# acc1 = Post('John Snow')
# acc2 = Post('Jamie Lannister')

# acc1.create_post('Good News', 'Moya sestra Sansa rodila dochku!!!', 'https://foro.jpg')
# acc1.create_post('Na progulke', 'Segodnya good weather, vyshel for walk!', 'https://foto123.jpg')
# acc1.create_post('Na chile!', 'Edu otdihat v Egipet', 'https://foto1.jpg')

# print(acc1.user)
# print(acc1.posts)

# print(acc1.retrieve_post(2))
# print(acc1.retrieve_post(5))

# print(acc1.update_post(2, title = 'Progulka updated', body = 'Segodnya obnovil progulku!', image = 'hhtps://image.jpg'))
# print(acc1.retrieve_post(2))
# print(acc1.delete_post(2))

# print(acc1.posts)
# print(acc2.user)
# print(acc2.posts)





# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'Меня зовут {self.name}, мне {self.age} лет.')
# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer
#     def info(self):
#         super().info()
#         print(f'Я учусь в университете {self.univer}')
# talgat = Student('Talgat', 17, 'MIT')
# talgat.info()
# print(talgat.name)

# class Class1:
#   def __init__(self, name, surname):
#     self.name = name
#     self.surname = surname
#   def info(self):
#     print(f'Меня зовут {self.name}')
#   def info1(self):
#     print(f'Фамилия - {self.surname}')

# class Class2(Class1):
#     def __init__(self, name, surname, univer, city):
#       super().__init__(name, surname)
#       self.univer = univer
#       self.city = city
#     def info(self):
#       super().info()
#       print(f'Я, {self.surname} {self.name}, учусь в {self.univer}')
#     def info1(self):
#       super().info1()
#       print(f'Я живу в городе {self.city}')
# talgat = Class2('Talgat', 'Asakeev', 'Harvard', 'Бишкек')
# talgat.info()
# talgat.info1()

# class A:
#   def __init__(self, stroka):
#     self.stroka = stroka
#   def method1(self):
#     print(self.stroka)
# class B(A):
#     def __init__(self, stroka, strok):
#        super().__init__(stroka)
#        self.strok = strok
#     def method1(self):
#        super().method1()
#        print(self.strok)
# talga = B('Основной функционал', 'Дополнительный функционал')
# talga.method1()

# class Str:
#   def __init__(self, string):
#     self.string = string
# class MyString(Str):
#   def __init__(self, string, append):
#     super().__init__(string)
#     self.append = append
#   def app(self):
#     example = self.append + self.string
#     return example
#   def pop(self):
#     return self.example.pop()
# ex = MyString('String')
# print(ex.app('hello'))
# print(ex.pop())
# print(ex)

# x = {1: 'HI', 2: 'Bye'}
# print(x.get())

# class MyDict(dict):
#   def __init__(self, dictionary):
#     self.dictionary = dictionary
#   def get(self):
#     for i in list((self.dictionary.keys())):
#       if list(self.dictionary.keys()[i]) == None:
#         print('Are you kidding?')
# ex = MyDict({1 : 'Hi', 2 : 'Bye'})
# ex.get()

# class MyDict(dict):
#   def get(self, dictionary, key, val):
#     return dictionary.get(val, 'Are you kidding?')
# ex = dict()
# exam = MyDict()

# class MyDict(dict):
#   def get(self, key, default = 'Are you kidding?'):
#     return dict.get(self, key, default)
# dict1 = MyDict(a = 3, b = 2, c = 1)
# print(dict1.get('d'))

# class MyString(str):
#   def append(self, stroka):
#     return stroka + stroka
#   def pop(self, stroka):
#     return stroka[:-1]
# ex = MyString('String')
# ex.append('hello')
# print(ex)
# print(ex.pop())
# print(ex)


    
# x = 'Hello0'
# y = x[:-1]
# print(y)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def display(self):
#     return f'Имя: {self.name}. Возраст: {self.age}'
# class Student(Person):
#   def __init__(self, name, age, fac):
#     super().__init__(name, age)
#     self.fac = fac
#   def display_student(self):
#     return f'Имя: {self.name}. Возраст: {self.age}. Факультет: {self.fac}'
# ex = Student('Талгат', 17, 'Информатика')
# print(ex.display())
# print(ex.display_student())


# class MyDict(dict):
#   def get(self, key, default = 'Are you kidding?'):
#     return dict.get(self, key, default)
# dict1 = MyDict(a = 3, b = 2, c = 1)
# print(dict1.get('d'))

# class ContactList(list):
#   def search_by_name(self, name):
#     matching = []
#     for contact in self:
#       if name in contact.name:
#         matching.append(contact)
#     return matching
# c1 = ContactList('Talgat')
# c2 = ContactList("Aiba")
# c3 = ContactList('Talgat')
# c1.search_by_name()
# c2.search_by_name()
# c2.search_by_name()
# from datetime import datetime
# class Smartphone:
#   def __init__(self, name, color, memory):
#     self.name = name
#     self.color = color
#     self.memory = memory
#     self.battery = 0
#   def str(self):
#     return f'Смартфон {self.name} с памятью {self.memory} гигабайт'
#   def charge(self, battery):
#     return self.battery + battery
# ex = Smartphone('Iphone 13', 'Gray', 256)
# print(ex.str())
# print(ex.charge(20))
# class Iphone(Smartphone):
#   def __init__(self, name, color, memory, ios):
#     super().__init__(name, color, memory)
#     self.ios = ios
#   def send_message(self):
#     return f'Всем привет! <Сообщение было отправлено со смартфона {self.name}>'
# class Samsung(Smartphone):
#   def __init__(self, name, color, memory, android):
#     super().__init__(name, color, memory)
#     self.android = android
#   def show_time(self):
#     curr_time = datetime.now()
#     return f'Текущее время: {curr_time}'
# tala = Iphone('Iphone 13', 'Gray', 256, 15.5)
# print(tala.send_message())
# talga = Samsung('Samsung Galaxy S22', 'White', 512, 11)
# print(talga.show_time())   
# 
# # class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'Меня зовут {self.name}, мне {self.age} лет.')
# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer
#     def info(self):
#         super().info()
#         print(f'Я учусь в университете {self.univer}')
# talgat = Student('Talgat', 17, 'MIT')
# talgat.info()
# print(talgat.name) 

# class Spell:
#   def __init__(self, name, formula):
#     self.name = name
#     self.formula = formula
#     self.desc = 'позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину'
#   def get_description(self):
#     return self.desc
#   def execute(self):
#     return f'{self.formula} {self.name}'
#   def __str__(self):
#     print(f'{self.formula} {self.name}\n{self}')
# ex = Spell('Alohomora', 'Открытие замков:')
# ex.get_description()
# ex.__str__()
# class Spell1(Spell):
#   def __init__(self, name, formula):
#     super().__init__(name, formula)
#   def get_description(self):
#     super().get_description()
#     return f'Огромный шар огня. Наносит большой урон.'
# class Spell:
#   def __init__(self, name, formula,desc):
#     self.name = name
#     self.formula = formula
#     self.desc = desc
#   def get_desc(self):
#     return self.desc
#   def execute(self):
#     return {self.formula},{self.name}
#   def __str__(self):
#     print(f'{self.formula} {self.name}\n{self.desc}')

# # ex = Spell('Alohomora', 'Открытие замков:', 'позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.')
# # ex.get_desc()
# # ex.__str__()
# class Spell1(Spell):
#   def __init__(self, name, formula, desc):
#     super().__init__(name, formula, desc)
#   def get_desc(self):
#     return super().get_desc()
#   def execute(self):
#     return super().execute()
#   def __str__(self):
#     return super().__str__()
# ex = Spell1('Alohomora', '1)Открытие замков:', 'позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.\n')
# ex1 = Spell1('Огненный Шар', '2)Стихия огня: ', 'Наносит большой урон по большой площади\n')
# ex2 = Spell1('Чидори', '3)Стихия молнии: ', 'Огромный урон по небольшой площади')
# # ex.get_desc()

# ex.__str__()
# ex1.__str__()
# ex2.__str__()


# class User:
#   def __init__(self, first_name, last_name, age, city):
#     self.name = first_name
#     self.last = last_name
#     self.age = age
#     self.city = city
#   def describe_user(self):
#     return f'Name: {self.name}. Last Name: {self.last}. Age: {self.age}. City: {self.city}'
#   def greet_user(self):
#     return f'Hi, {self.name}!'
# class Admin(User):
#     def __init__(self, first_name, last_name, age, city, privileges):
#       super().__init__(first_name, last_name, age, city)
#       self.priv = privileges
#     def show_privileges(self):
#         return f'Доступные привелегии: {self.priv}'
# ex = Admin('Talgat', 'Asakeev', 17, 'Bishkek', ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей'])
# print(ex.describe_user())
# print(ex.greet_user())
# print(ex.show_privileges())


# class Spell:
#   def __init__(self, name, formula,desc):
#     self.name = name
#     self.formula = formula
#     self.desc = desc
#   def get_desc(self):
#     return self.desc
#   def execute(self):
#     return {self.formula},{self.name}
#   def __str__(self):
#     print(f'{self.formula} {self.name}\n{self.desc}')


# class Spell1(Spell):
#   def __init__(self, name, formula, desc):
#     super().__init__(name, formula, desc)
#   def get_desc(self):
#     return super().get_desc()
#   def execute(self):
#     return super().execute()
#   def __str__(self):
#     return super().__str__()
# ex = Spell1('Alohomora', '1)Открытие замков:', 'позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.\n')
# ex1 = Spell1('Огненный Шар', '2)Стихия огня: ', 'Наносит большой урон по большой площади\n')
# ex2 = Spell1('Чидори', '3)Стихия молнии: ', 'Огромный урон по небольшой площади')


# ex.__str__()
# ex1.__str__()
# ex2.__str__()

  
