# ООП(объектно-ориентированное-программирование) - цель создания была связать поведение объекта с ее данными.

# Класс - это описание того, какими свойствами(данными) и поведением(функциями) должен обладать объект(экземпляр).
# Объект - это экземпляр класса с собственным состоянием этих свойств.

# Свойствами называют обычные переменные.
# (name ='John', height = 185)

# Поведение это обычные функции(def eat - методы)
#----------------------------------------------------------------------------------

# kirk = ['James Kirk', 34, 'Captain', 2000]
# snow = ['John Snow', 28, 'Police Officer', 1500]
# mccoy = ['Leonard Mccoy', 'Chief', 1700]

# for object in [kirk, snow, mccoy]:
#     print(object[1])

# class Human():
#     def __init__(self,name,age,job,salary):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.salary = salary
#     def show_info(self):
#         return f'Name: {self.name},\nAge: {self.age}, \nJob: {self.job}, \nSalary: {self.salary}.\n'
# kirk = Human('James Kirk', 34, 'Captain', 2000)
# snow = Human('John Snow', 28, 'Police Officer', 1500)
# mccoy = Human('Leonard Mccoy', 25, 'Chief', 1700)

# print(kirk.show_info())
# print(snow.show_info())
# print(mccoy.show_info())

# class Dog():
#     #атрибуты класса
#     ushi = 'Есть уши'
#     age = 0

#     def __init__(self, name, color):
#         '''
#         Инициализатор.
#         Именно здесь определяются атрибуты объекта класса
#         '''
#         #В self хранится сам объект 
#         self.name = name #Атрибут экземпляра(объекта) класса
#         self.color = color
# bobik = Dog('Bobik', 'brown')
# yumi = Dog('Yumi', 'white')
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, {bobik.ushi} ')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, {yumi.ushi} ')
# bobik.age = 2
# yumi.age = 1
# bobik.ushi = 'Нет ушей'
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, {bobik.ushi} ')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, {yumi.ushi} ')
#-----------------------------------------------------------------------------------------

# class Human:
#     def __init__(self, name, weight, nationality):
#         self.name = name
#         self.age = 0
#         self.weight = weight
#         self.nation = nationality
#     def birthday(self):
#         import random
#         print(f'\nHappy birthday {self.name}')
#         self.age += 1 #self.age = self.age + 1
#         self.weight += random.randint(3,7)
# human1 = Human('John', 3.700, 'American')
# human2 = Human('Abu-bakr', 3, 'Arabian')
# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After 1 year:')
# human1.birthday()
# human2.birthday()

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After 3 month')
# human1.birthday()
# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

#----------------------------------------------------------------------------------------
# class Student:
#     univer = 'MIT'

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last = last_name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False
    
#     def add_point(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             self.is_ready_to_work = True
#             print(f"{self.name} is ready to work.")
    
#     def read_book(self,book):
#         self.books.append(book)
#         self.add_point(50)
    
#     def do_lab_works(self):
#         self.add_point(50)
    
#     def do_real_projects(self):
#         self.add_point(100)

#     def learn_new_languages(self, language, point):
#         if not 60 < point <= 100:
#             raise Exception('Your point out of range')
#         self.languages.update({language : point})
#         self.add_point(point)
# st1 = Student('John', 'Snow')
# st2 = Student('Jamie', 'Lannister')
# print(st1.name)
# print(st2.name)
# print(f'Before study {st1.name}:', st1.books, st1.languages, st1.knowledge, st1.is_ready_to_work)

# st1.read_book('Game of Thrones')
# st1.read_book('Martin Iden')
# st1.read_book('Eugene Onegin')
# st1.read_book('Ants')

# st1.do_real_projects()
# st1.do_lab_works()
# st1.do_lab_works()
# st1.learn_new_languages('Python', 90)
# st1.do_real_projects()
# st1.learn_new_languages('JS', 100)

# print(st1.name, st1.books, st1.knowledge, st1.languages, st1.is_ready_to_work)
# print(st1.univer)

# class Salary:
#     tax = 0.15

#     def __init__(self, salary, exp):
#         self.salary = salary
#         self.age_of_work = exp

#     def sum_of_tax(self):
#         res = (self.salary * self.tax) * (self.age_of_work * 12)
#         print(f'Сумма налога составила {res} сомов, за {self.age_of_work} лет работы')
# john = Salary(150000, 8)
# john.sum_of_tax()

# x = input('Напишите "Привет": ').lower()
# if x == 'привет':
#   z = input('Выберите офис:\n1)google_kazakstan\n2)google_paris\n3)google_poland\n4)google_kyrgyzstan\n5)google_san_francisco\n6)google_germany\n7)google_moscow\n8)google_sweden\n')
#   if z == "1":
#     kz = input("Напишите вашу жалобу: ")
#     with open("google.kazakstan.txt","a") as file:
#       file.writelines(kz)
#   elif z == "2":
#     fr = input("Напишите вашу жалобу: ")
#     with open("google_paris.txt","a") as file:
#       file.writelines(fr)
#   elif z == "3":
#     pl = input("Напишите вашу жалобу: ")
#     with open("google_poland.txt","a") as file:
#       file.writelines(pl)
#   elif z == "4":
#     kg = input("Напишите вашу жалобу: ")
#     with open("google_kyrgyzstan.txt","a") as file:
#       file.writelines(kg)
#   elif z == "5":
#     us = input("Напишите вашу жалобу: ")
#     with open("google_san_francisco.txt","a") as file:
#       file.writelines(us)
#   elif z == "6":
#     gr = input("Напишите вашу жалобу: ")
#     with open("google_germany.txt","a") as file:
#       file.writelines(gr)
#   elif z == "7":
#     ru = input("Напишите вашу жалобу: ")
#     with open("google_moscow.txt","a") as file:
#       file.writelines(ru)
#   elif z == "8":
#     sw = input("Напишите вашу жалобу: ")
#     with open("google_sweden.txt","a") as file:
#       file.writelines(sw)
    
  
# array = [
#  'google_kazakstan.txt'
# , 'google_paris.txt'
# , 'google_poland.txt'
# , 'google_kyrgyzstan.txt'
# , 'google_san_francisco.txt'
# , 'google_germany.txt'
# , 'google_moscow.txt'
# , 'google_sweden.txt'
# ]
# x = input('Напишите "Привет": ').lower()
# if x == 'привет':
#     print('Выберите офис:')
#     for i in array:
#         print(f'{array.index(i) + 1}) {i}')
#     z = input()
#     for file in array:
#         if int(z) == array.index(file) + 1:
#             example = input("Напишите вашу жалобу: ")
#             with open( file , 'a') as file:
#                 file.writelines(f'\n{example}')

# for i in array:
#     print(array.index(i))

# class Nobel:
#   def __init__(self, category, year, winner):
#     self.category = category
#     self.year = year
#     self.winner = winner
#   def get_year(self):
#     nowYear = 2021
#     return (nowYear - self.year)
# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

# print(15%10)
    
# data = dict()
# i = 0
# while i < 3:
#     key = input('введите ключ: ')
#     value = input('введите значение: ')

#     data[key] = value
# i += 1
# print(data)

# i = 0
# while i < 3:
#   todo = input('Что вы хотите сделать?\n1)Сходить в кино\n2)Сделать домашнее задание\n3)Выгулять собаку\n1 2 3:\n').lower()
#   priority = input('Какой приоритет?\n1.\n2.\n3.\n')
#   class ToDo:
#     ls = []
#     def __init__(self, cinema, HW, walk_the_dog):
#       self.cinema = cinema
#       self.hw = HW
#       self.dog = walk_the_dog
#     def give_priority(self):
#       d = dict()
#       if todo == '1':
#         d[priority] = self.cinema
#       elif todo == '2':
#         d[priority] = self.hw
#       elif todo == '3':
#         d[priority] = self.dog
#       ls = []
#       ls.append(d)
#       return ls
#   t = ToDo('Сходить в кино', 'Сделать домашнее задание', 'Выгулять собаку')
#   print(t.give_priority())
#   i += 1


# import math
# class Math:
#   def __init__(self,num):
#     self.num = num
#   def fact(self):
#     return math.factorial(self.num)
#   def sum(self):
#     sum = 0
#     fakeNum = self.num
#     while(fakeNum != 0):
#       sum = sum + fakeNum % 10
#       fakeNum = fakeNum // 10
#     return sum
#   def mul(self):
#     for i in range(1,11):
#       print(self.num, 'x', i, '=', self.num * i)
# num1 = Math(13)
# print(num1.fact())
# print(num1.sum())
# num1.mul()


# y = set('@#&$%!~*')
# x = 'talga1@1111'
# if x.isalnum() and 8 <= x < 15 and any (x in y):
#   print('Пароль сохранен')
# else:
#   print('Не подходит')

# chars = set('0123456789$,')
# if any((c in chars) for c in '$'):
#     print('Found')
# else:
#     print('Not Found')

# x = 'talga@111#'
# y = "@#&$%!~*"
# for i in x:
#   if i in y and len(x) > 5:
#     print('yes')

# fullstring = "StackAbuse"
# substring = "tack"

# if substring in fullstring:
#     print("Found!")
# else:
#     print("Not found!")

# x = '123talga'
# if all(i.isalnum() and len(x)>5  for i in x ):
#   print('yes')
# else:
#   print('no')


# class ToDo:
#   def __init__(self, cinema, HW, walk_the_dog):
#       self.cinema = cinema
#       self.hw = HW
#       self.dog = walk_the_dog
#   def give_priority(self):
#     self.cinema = {3:self.cinema}
#     self.hw = {2:self.hw}
#     self.dog = {1:self.dog}
#     z = (self.cinema,self.hw,self.dog)
#     return (z)
#   def ls(self):
#     return sorted(self.z, key = max, reverse = True)
# tal = ToDo('Сходить в кино', 'Сделать дз', 'Выгулять собаку')
# print(tal.give_priority())
# print(tal.ls())



# from string import ascii_letters


# class Password:
#   def __init__(self, password):
#     self.password = password
#   def validate(self):
#     if 15 > len(self.password) > 7:
#       has_number = 0
#       has_symbol = 0
#       has_letter = 0
#       symbols = ['@', '#', '&', '$', '%', '!', '~', '*']
#       for i in self.password:
#         if i.isdigit(): has_number += 1
#         if i in symbols: has_symbol += 1
#         if i in ascii_letters: has_letter += 1
#       if has_number > 0 and has_symbol > 0 and has_letter > 0:
#         return 'Ваш пароль сохранен'
#       else:
#         return 'Пароль не подходит'
#     else:
#       return 'It has to be more than 7 and less than 15'
#   def __str__(self):
#     return '*' * len(self.password)
# psw = Password('talga123@@')
# print(psw.validate())
# print(psw.__str__())

