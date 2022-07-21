#############    Переменных класса и экземпляра    #############

'''
При изучении объектно-ориентированного программирования на Python может возникнуть несколько сложностей, когда дело доходит до разграничения переменных класса и экземпляра. Давайте разберем разницу между переменными класса и экземпляра и посмотрим примеры, демонстрирующие различные варианты использования.

Во-первых,помним что классы часто представляют что-то в реальном мире, так что представьте, хотите ли вы создать класс, списка студентов. Вы можете создать класс с именем Student, который представляет собой шаблон, который определяет различные атрибуты студента. Таким образом, каждый студент является экземпляром класса Student.

При работе с данными любого типа некоторые атрибуты будут уникальными, а некоторые будут общими. Рассмотрим пример с учениками: у каждого учащегося в этом классе один и тот же номер и один учитель, но у каждого из них есть уникальное имя, возраст и любимый предмет.

Переменные класса.
Переменные класса обычно являются переменными, которые являются общими для всех экземпляров. И они определены так:
'''

# class Student:
#    teacher = 'Gulzana eje'  # переменная класса

'''
Каждый экземпляр класса будет иметь одинаковое значение для этих переменных:
'''

# adinay = Student()
# semetey = Student()

# print(adinay.teacher)
# # Gulzana eje

# print(semetey.teacher)
# # Gulzana eje

'''
Переменные экземпляра.
Переменные экземпляра (также называемые атрибутами данных) уникальны для каждого экземпляра класса и определяются в методе класса, например:
'''

# class Student:
#    teacher = 'Mrs. Jones'  # переменная класса   

#    def __init__(self, name):
#        self.name = name  # переменная экземпляра

'''
Посмотрите, как каждый экземпляр теперь содержит уникальное значение name:
'''

# adinay = Student('Adinay')
# semetey = Student('Semetey')

# print(adinay.name)
# # Adinay

# print(semetey.name)
# # Semetey

'''
Чего ожидать от переменных класса.
Переменные класса являются общими для всех экземпляров класса. Напоминаем, что они определены так:
'''

# class Student:
#    teacher = 'Gulzana eje'

'''
Иными словами, переменные класса ссылаются на одно и то же место в памяти. Смотрите следующее:
'''

# adinay = Student()
# semetey = Student()

# print(id(adinay.teacher) == id(semetey.teacher))
# # True
# # Функция id возвращает адрес объекта в памяти для реализации CPython.

'''
Таким образом, с помощью функции id мы можем подтвердить, что атрибут teacher ссылается на то же место в памяти.

Изменение переменной класса
Что произойдет, если мы изменим переменную класса даже после создания экземпляров?
'''

# adinay = Student()
# print(adinay.teacher)
# # Gulzana eje

# Student.teacher = 'Adilet baike'
# print(adinay.teacher)
# # Adilet baike

'''
Как и следовало ожидать, поскольку переменная teacher ссылается на общее местоположение в памяти, она также обновляется в экземпляре.

Изменение переменной экземпляра.
Это, вероятно, наиболее очевидное и ожидаемое поведение. Но я все же покажу несколько примеров для полноты.

Рассмотрим наш класс Student с переменными класса и экземпляра:
'''

# class Student:
#    teacher = 'Gulzana eje'

#    def __init__(self, name):
#        self.name = name

'''
Мы видим, что каждый экземпляр класса имеет уникальный адрес памяти для имени:
'''

# adinay = Student('Adinay')
# kuba = Student('Kuba')

# print(id(adinay.name) == id(kuba.name))
# # False

'''
Как и следовало ожидать, обновление атрибута name в одном экземпляре не влияет на другой:
'''

# print(adinay.name)
# # Adinay

# print(kuba.name)
# # Kuba

# kuba.name = 'Kubat'
# print(kuba.name)
# # Kubat

# print(adinay.name)
# # Adinay

'''
Переменные экземпляра переопределяют переменные класса (и методы).
Важно отметить, что переменные экземпляра (или атрибуты данных) переопределяют переменные класса.

Помните следующее?
'''

# print(id(adinay.teacher) == id(kuba.teacher))

'''
Что произойдет, если мы изменим атрибут teacher прямо в одном из случаев:
'''

# adinay.teacher = 'Adilet baike'

'''
Это важно отметить: переменные экземпляров не нужно объявлять, они создаются всякий раз, когда им присваиваются, а переменные экземпляра переопределяют переменные класса. Это означает, что в экземпляре Tom teacher больше не ссылается на переменную класса, а ссылается на вновь созданную переменную экземпляра.

И, естественно, экземпляр Сьюзен не затронут:
'''

# print(adinay.teacher)
# # Adilet baike

# print(kuba.teacher)
# # Gulzana eje

'''
Надеюсь, вы видите, как такое поведение может привести к путанице. По этой причине важно сохранять организованные имена переменных. Если переменная объявлена как переменная класса, она (обычно) не должна быть переопределена. Переменные экземпляра могут быть определены в очевидных местах, например, метод __init__. Часто хорошо придумать соглашение об именовании переменных. Например, методы класса должны быть глаголами, существительными переменных класса и существительными переменных экземпляра с префиксом «_».

Использование изменяемых объектов в качестве переменных класса.
В связи с предыдущим шагом, будьте осторожны при использовании изменяемых объектов в качестве переменных класса. Вы можете получить не то, чего ожидаете.

Представьте, что мы хотим получить список результатов тестов студента. Мы могли бы составить такой класс:
'''

# class Student:
#    teacher = 'Gulzana eje'
#    test_scores = []

#    def __init__(self, name):
#        self.name = name

#    def add_score(self, score):
#        self.test_scores.append(score)

'''
У нас есть переменная класса для хранения баллов, и у нас есть метод класса для добавления баллов. Теперь давайте добавим несколько баллов.
'''

# adinay = Student('Adinay')
# semetey = Student('Semetey')

# adinay.add_score(90)
# semetey.add_score(100)

# print(adinay.test_scores)
# # [90, 100]

'''
Как вы заметили, мы сделали ошибку. test_scores - это переменная класса, а не переменная экземпляра. Каждый экземпляр просто добавляет значения в переменную класса. А мы хотим, чтобы каждый экземпляр содержал свой собственный список test_scores.

Так что класс может выглядеть так:
'''

# class Student:
#    teacher = 'Gulzana eje'

#    def __init__(self, name):
#        self.name = name
#        self.test_scores = []

#    def add_score(self, score):
#        self.test_scores.append(score)

'''
И теперь наша проблема решена!
'''

# adinay = Student('Adinay')
# semetey = Student('Semetey')

# adinay.add_score(90)
# semetey.add_score(100)

# print(adinay.test_scores)
# # [90]
# print(semetey.test_scores)
# # [100]



# class Coder:
#   count_code_time = 0
#   def __init__(self, hours):
#     self.hours = hours
#   def get_info(self):
#     pass
#   def coding(self):
#     pass
# class Backend(Coder):
#   def __init__(self, hours):
#     super().__init__(hours)
#   languages_backend = 'Python, Java'
#   def get_info(self):
#     super().get_info()
#     print(f'Языки программирования: {self.languages_backend}')
#   def coding(self):
#     super().coding()
#     self.count_code_time += self.hours
#     print(self.count_code_time)
# class Frontend(Coder):
#   languages_frontend = 'JS'
#   def get_info(self):
#     super().get_info()
#     print(f'Языки программирования: {self.languages_frontend}')
#   def coding(self, hours):
#     super().coding()
#     self.hours += self.count_code_time
#     print(self.count_code_time)
# class FullStack(Backend, Frontend):
#   languages_backend = 'Python, Java'
#   languages_frontend = 'JS'
#   def get_info(self):
#     super().get_info()
#     print(f'Языки программирования: {self.languages_frontend},{self.languages_backend}')
#   def coding(self, hours):
#     super().coding()
#     self.hours += self.count_code_time
#     print(self.count_code_time)
# back = Backend(100)
# # front = Frontend()
# # fs = FullStack()
# back.get_info()
# back.coding()
# back.coding()
# back.coding()


# class Square:
#   def __init__(self, len, height):
#     self.len = len
#     self.height = height
#   def sq(self):
#     return self.len * self.height
# class Triangle:
#   def __init__(self, len):
#     self.len = len
#   def sq(self):
#     return 0,5 * self.height * self.len
# class Pyramid(Square, Triangle):
#   def __init__(self, len, height):
#     super().__init__(len, height)
#   def get_volume(self):
#     return 1/3 * self.len ** 2 * self.height
# obj = Pyramid(10, 4)
# print(obj.get_volume())
# print(obj.sq())

# print(0.5 * 4 * 10)


class Square:
  def __init__(self, len, height):
    self.len = len
    self.height = height
  def sq(self):
    return self.len * self.height
class Triangle:
  def __init__(self, len):
    self.len = len
  def sq2(self):
    return 0.5 * self.height * self.len
class Pyramid(Square, Triangle):
  def __init__(self, len, height):
    super().__init__(len, height)
  def get_volume(self):
    return 1/3 * self.len ** 2 * self.height
obj = Pyramid(10, 4)
print(f'Объем пирамиды: {obj.get_volume()}')
print(f'Площадь квадрата: {obj.sq()}')
print(f'Плошадь треугольника: {obj.sq2()}')

class AreaMixin:
    def area(self):
        return self.len*(self.len + 2 * self.height)
class Cube(Square, AreaMixin):
    def __init__(self, len, height):
      super().__init__(len, height)
obj3 = Cube()
print(obj3.area())
  