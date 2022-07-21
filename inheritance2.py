# Множественное наследовоание - это когда класс наследуется от двух или более классов.

# MRO(Method Resolution Order) - поиск родительских классов. Был создан для того чтобы решить проблему ромба.

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')
#     def ride(self):
#         print('We are riding on the ground')
# class Plane:
#     def fly(self):
#         print('We are flying')
#     def play_music_at_station(self):
#         print('We started listen to music')
    
# class FutureAuto(Plane, Auto):
#     pass
# obj1 = FutureAuto()
# obj1.fly()
# obj1.ride()
# obj1.play_music_at_station()

#--------------------------------------------------------------
# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     def say(self):
#         print('class First')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class Third(First, Second):
#     def say(self):
#         super().say()
#         print('class Third')
# obj = Third()
# obj.say()

# print(Third.__mro__)

#-----------------------------------------------------------

# class Y:
#     pass
# class X:
#     pass
# class A(X,Y):
#     pass
# class B(Y,X):
#     pass
# class MyMRO(type):
#     def mro(cls):
#         return(cls, A, B, X, Y, object)
# class C(A,B, metaclass=MyMRO):
#     pass
# obj = C()
# print(C.__mro__)
#-----------------------------------------------------------

# Mixins(Миксины)
# class MusicPlayerMixin:
#     def play_music_on_station(self):
#         print('Music is playing')
# class Machines:
#     def start_engine(self):
#         print('Started engine')
# class Auto(Machines, MusicPlayerMixin):
#     pass
# class Plane(Machines, MusicPlayerMixin):
#     pass
# class SmartClock(Machines, MusicPlayerMixin):
#     pass
# class Microwave(Machines):
#     pass


# obj_auto = Auto()
# obj_plane = Plane()
# obj_clock = SmartClock()
# obj_microwave = Microwave()
# obj_plane.start_engine()
# obj_auto.play_music_on_station()
# obj_clock.start_engine()

