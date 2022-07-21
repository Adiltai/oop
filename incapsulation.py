# Инкапсуляция: 
# 1. Связь данных с методами которые этими данными управляют.
# 2. Набор инструментов для управления доступа к методам и данным.

# Инкапсуляция как связь
# class Phone:
#     number = '+996 707 707 707'
#     def print_number(self):
#         print(f'Мой номер: {self.number}')
# myphone = Phone()
# myphone.print_number()

# Инкапсуляция как сокрытие данных
# Уровни доступа в питоне:
# 1.Публичный(public, age)
# 2.Защищенный(protected, _age)
# 3.Приватный(private, __age)

# class Phone:
#     username = 'John' #public
#     _caller = 'Mike' #protected
#     __count_rings = 0 #private

#     def call(self):
#         print(f'Тебе звонит: {self._caller}!')
#     def __turn_on(self):
#         self.__count_rings += 1
#         print(f'Вы созванивались {self.__count_rings}')
# # phone = Phone()
# # phone.call()
# # print(phone._caller)
# # phone._Phone__turn_on()
# # print(phone._Phone__count_rings)
# class Number(Phone):
#     pass
# number = Number()
# print(number.username)
# print(number._caller)

# class Test(Number):
#     pass
# test = Test()
# print(test.username)
# print(test._caller)

#getter & setter
# Они используются для получения и установки значения, чтобы добавить логику проверки при получении данных.
# Еще чтобы избежать прямого доступа к защищенному атрибуту класса.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_info(self):
#         print(f'Name: {self.name}\nAge: {self.age}')
# john = Person('John', 23)
# print(john.name)
# print(john.age)
# john.display_info()
# john.age = -18
# john.display_info()

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 0
    
#     def display_info(self):
#         print(f'Name: {self.name}\nAge: {self.__age}')
    
#     def set_age(self, age): #setter
#         if 0 < age < 140: self.__age = age
#         else: print('Invalid age!')
#     def get_age(self):
#         print(self.__age)
# john = Person('John')
# john.display_info()
# john.set_age(5)
# john.set_age(-18)
# john.set_age(6)
# john.get_age()


# class Car:
#   __speed = 0
#   @__speed.setter
#   def set_speed(self, speed):
#     self.__speed = speed
#   @property
#   def show_speed(self):
#     print(f'Скорость машины = {self.__speed} км/час')
# car = Car()
# speed = 120
# print(speed)

# class Car:
#   __speed = 0
#   @property
#   def show_speed(self):
#     # return f'Скорость машины = {self.__speed} км/час'
#     print(self.__speed)
#   @speed.setter
#   def set_speed(self, speed):
#     speed.__speed = speed
# car = Car()
# car.speed = 120
# print(car.speed)
# class Car:
#     __speed = 0
    
    
#     @property
#     def show_speed(self):
#         print(f'Скорость машины = {self.__speed} км/час')
    
#     @show_speed.setter
#     def set_speed(self, speed):
#         self.__speed = speed
# car = Car()
# car.speed = 120
# print(car.speed)

# Аннотации свойств
# @property

# class Person:
#     __name = 'John'
#     __age = 25
#     @property
#     def name(self):
#         print(self.__name)
#     @name.setter
#     def name(self, name):
#         self.__name = name
#     @property
#     def age(self):
#         print(self.__age)
#     @age.setter
#     def age(self, age):
#         if 0 < age < 140:
#             self.__age = age
#         else:
#             print('Недопустимый возраст!')
# obj = Person()
# obj.name #obj.get_name()
# obj.name = 'Tom' #object.set_name('Tom')
# obj.name
# obj.age
# obj.age = 18
# obj.age
# obj.age = 1000
# obj.age = 25
# obj.age 


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
# заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
# заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# from datetime import datetime, timedelta
# from time import sleep
# class Phone:
#     def __init__(self, imei, os):
#         self.__imei = imei
#         self.__os = os
#         self.__battery_leevel = 100
    
#     def get_info(self):
#         if self.__battery_leevel <= 0:
#             raise Exception('Телефон разряжен')
#         self.__battery_leevel -= 0.5
#         print(f'OS: {self.__os}\nIMEI: {self.__imei}')
    
#     def play_music(self):
#         if self.__battery_leevel <= 5:
#             raise Exception('Телефон разряжен')
#         self.__battery_leevel -= 5
#         print('Слушаем Атабекова')
    
#     def play_video(self):
#         if self.__battery_leevel <= 10:
#             raise Exception('Телефон разряжен')
#         self.__battery_leevel -= 7
#         print('Смотрим Топлес')
#     def charge_battery(self, sec):
#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')
#         # print(now())
#         # print(end_time)
#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__battery_leevel < 100:
#                 self.__battery_leevel += 1
#             print(f'Идет зарядка\nВаш уровень батареи: {self.__battery_leevel}')
#             if self.__battery_leevel >= 100:
#                 print('Телефон полностью заряжен')
# obj = Phone(123456789, 'Android')
# obj.play_video()
# obj.play_video()
# obj.charge_battery(15)

# from datetime import datetime
# from time import sleep
# class Clock:
#     def NowTime():
#         current_time = datetime.now()
#         return (f'Время: {current_time.hour}:{current_time.minute}:{current_time.second}')
# class Alarm:
#     def alarm_on():
#         print(f'Будильник! {Clock.NowTime()}')
#     def alarm_off():
#         print('Будильник выключен')
# class AlarmClock(Clock, Alarm):
#     def set_alarm(alarm_timer):
#         while True:
#             sleep(1)
#             print(super().NowTime())
#             if super().NowTime() == alarm_timer:
#                 print(super().alarm_on())
# alarm_timer = datetime.time(4, 1, 59)
# obj = AlarmClock()
# obj.set_alarm()
        

# curr = datetime.now()
# print(type(str(curr)))

# obj = AlarmClock
# obj.set_alarm()

# obj = Alarm()
# obj.alarm_on()
# obj.alarm_off()

# from tkinter import 
# import datetime
# import time
# import winsound

# def alarm(set_alarm_timer):
#     while True:
#         time.sleep(1)
#         current_time = datetime.datetime.now()
#         now = current_time.strftime("%H:%M:%S")
#         date = current_time.strftime("%d/%m/%Y")
#         print("The Set Date is:",date)
#         print(now)
#         if now == set_alarm_timer:
#             print("Time to Wake up")
#         winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
#         break

# def actual_time():
#     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
#     alarm(set_alarm_timer)

        

    


    
    



    


    
    
   




