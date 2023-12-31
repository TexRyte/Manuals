import random as rand # Импорт библиотеки рандома (as - как (rand.randint, как пример использования.)).
import random as random
from math import sqrt, sin # Импорт объекта или объектов из библиотеки.
import math
from turtle import * # Импорт всех объектов из библиотеки. (Не рекомендуется.)
import itertools
import re
import this # Дзен языка Python или PEP 20. Не используется, ибо после добавления этой строки, автоматом выводит текст в консоль.
import tkinter

###################################################################################################################################

# Правила написания в Python (PEP 8):

# import module - имена модулей должны быть короткими и маленькими буквами.

class MyClass: # В именах класса все слова начинаются с больших букв.
    pass

name_of_tea = "Green Tea" # Переменные пишутся маленькими буквами с нижним подчеркиванием

TEA_NAME = "const" # Константы пишутся заглавными буквами с нижними подчеркиваниями.

if_ = "if" # Имена, которые пересекаются с ключевыми словами python, должны иметь замыкающее подчеркивание.

"""

- Строки не должны быть длинее 80 символов.
- Избегать from module import *
- В строке должно быть не более одной инструкции.

Когда нужно - можно игнорировать правила PEP 
(Например другой единый стиль написания кода, над которым работают несколько человек,
или когда ввиду правил PEP усложняется читаемость кода даже для разработчика этого самого кода.) 

"""



###################################################################################################################################


print ("Hello, python") # Функция вывода.

print("Iron", "Man", sep="-") # Разделение.

# Объявление переменных:
a = 1 # Int - целое значение.
b = "" # String - текст.
c = True # Boolean - булевая логика.
d = 1.1 # Float - значение с плавающей запятой.

# Простые операции:
b = 1

a = a + b # Сложение.
a = a - b # Вычитание.
a = a / b # Деление.
a = a // b # Деление нацело.
a = a * b # Умножение.
a = a ** b # Возведение в степень.
a = a % b # Нахождение остатка от деления.
# Упрощенный вариант:
a += b 
a -= b 
a /= b 
a //= b
a *= b 
a **= b
a %= b 


# Оператор Walrus
# Позволяет работать с переменной, которой еще не существует.

print(num:=int(input("Enter your number: "))) # Один из вариантов использования. 

# Работа со строками:

string = "String" # Создание строки. Создавать можно и с 'String' - разницы не будет.
string = "\n" # Перенос строки.
string = "\t" # Отступ (Tab).
string = 'He\'s' # Когда нужно поставить апостров в текст.
string = "Hi" + "!" # Контентенация.
string = "ba" + ("na" * 2) # Умножение строки.

string = "Hello world!"
print(string[3]) # Вывод элемента по индексу (l).
print(string[6:11]) # Вывод диапазон элементов по индексу (world).
print(string[5:]) # Другой вариант (world!).
print(string[-3]) # Вывод элемента по индексу, начиная с конца (r).
print(string[::3]) # Переступает через n количество символов (3) (hlwl).
print(string.lower()) # Все буквы маленькие.
print(string.upper()) # Все буквы заглавные.
print(string.title()) # Каждое новое слово с заглавной буквы.
print(string.capitalize()) # Первая буква строки заглавная.
print(string.swapcase()) # Все буквы меняют регистр.
print(string.startswith("s")) # Отвечает, наичнается ли строка с указаной буквы.
print(string.endswith("2")) # Отвечает, заканчивается ли строка с указаной буквы.
print(string.isalnum()) # Отвечает на вопрос, все ли символы в строке цифры и/или буквы.
print(string.isdigit()) # Отвечает на вопрос, все ли символы в строке цифры.
print(string.isalpha()) # Отвечает на вопрос, все ли символы в строке буквы.
print(string.count("na")) # Возвращает кол-во совпадений.
string.replace("Hello", "Hi") # Замена всех совпадающих элементов.
words = string.split() # Делает список, разделяя элементы по индексам. (["1", "2", "3"])
print(", ".join(["spam", "eggs", "ham"])) # Разделяет каждый элемент строкой ("spam, eggs, ham")

# Работа с числами
print(max(1, 2, 3)) # Выводит максимальное значене. 
print(min(1, 2, 3)) # Выводит минимальное значене.
print(abs(-99)) # Расстояние до нуля (99).

# Комментарии

# Комментарий в одной строке.
"""
Комментарий в нескольких строках.
"""

# Функция ввода input()

x = input() # Простейший вариант.
x = input("Hello, user! Write your text, please: ") # Можно добавить текст, чтобы вывести его пользователю.
x = int(input("Write your number: ")) # Можно поставить функцию, для изменения типа данных. x == int.

# Логические операторы

# Операторы сравнения
# Сравнение строк происходит за алфавитным расположением буквы. Т.е. если А и Б сравнить, то А будет больше, ибо стоит первее.

# a == a - Равно.
# a != a - Не равно.
# a <= a - Больше или равно.
# a >= a - Меньше или равно.
# a > a - Больше. 
# a < a - Меньше.

# Оператор if
a = 1
b = 1

if a == b: # Выполняется, если условие истинно.
    print(a + b) # Инструкция.
elif a > b: # Замена цепочке else: if ... 
    print(a - b) # Инструкция.
else: # Если ни одно из условий не подошло.
    print(a ** b) # Инструкция

# or, and, not

# or - Или.
# # and - И.
# not - Нет.

# Тернарный оператор

a = 7
b = 1 if a >= 5 else 42 # Де-факто if в одну строку. b = 1, если условие истинно, и 42, если ложно.
print(b)


# Списки
# Итерируемый объект, который может содержать в себе различные значение в различных порядка. Все значения имеют свой индекс.

words = ["Hello", "world", "!"] # Создание списка.
print(words[0]) # Вывод первого значение.
words[0] = "Hi" # Замена элемента.
print(words * 2) # Можно проводить такие же простые операции, как и над строками.

if "Hi" in words: # in - оператор для проверки наличия чего-либо в списке.
    print ("True!") 
words.append("How are you?") # append - добавляет новое значение в конец.

print(len(words)) # len - возвращает кол-во значений.

words.insert(1, "QQ") # Добавляет значение в выбранную позицию.
print (words.index("Q")) # Находит первое значение в списке.

print(max(words)) # Возвращает максимальное значение из списка.
print(min(words)) # Возвращает минимальное значение из списка.
print(words.count("Q")) # Возвращает кол-во упоминаний элемента в списке.
words.remove("Q") # Удаляет объект из списка.
words.reverse() # Располагает элементы списка в обратном порядке.
nums = [1, 2 , 3]
nums = sum(nums) # Сумма всех элементов.
words.sort(reverse=True) # Сортирует список в порядке возрастания. reverse=True - В обратном порядке.

# Списковое включение

cubes = [i ** 3 for i in range(5) if i**2 % 2 == 0] # Простое условие.
print(cubes)


# While 
# Цикл, который используется в случае, когда НЕ знаем кол-во итераций. Работает пока выражение истинно.

a = 0
while a < 5: # Объявление цикла while.
    print(a) # Инструкция, выполняемая при каждой итерации.
    a += 1

# for
# Цикл, который используется в случае, когда известно кол-во итераций. 

words = ["united", "kingdom", "of", "great", "britain"]

for word in words: # Объявление цикла for.
    word.capitalize() # Инструкция.
print(words)

# else
# Помимо конструкции if, else можно использовать с циклами for и while.

q = 1

while True:
    if q == 10:
      break # Прерывает цикл и вызов else.
    q += 1

else:
    print("Unbroken") # Вызывается, после "нормального" окончания работы цикла (break не вызывает его).

# continue и break работают в обоих циклах. continue - следующая итерация, break - прервать цикл.

# range

num = list(range(10)) # Можно создать последовательный список от 0 до 9.
num = list(range(7, 15)) # Можно создать последовательный список от 7 до 14.
num = list(range(5, 20, 2)) # Третий аргумент - интервал. (5, 7, 9 ... 19)
for i in range(5): # Воспроизведение инструкции 5 раз.
    print("Hello!") # Инструкция.

# Функции

def my_func(): # Объявление функции (Получить аргумент).
    print("spam" * 3) # Инструкция.
    a = 1
    return a # Возврат значение из функции.
    # Всё, что написано после return - не будет выполняться.
# Функция сперва объявляеться, позже вызываеться. НЕ иначе.
my_func() # Вызов функции (Передать аргумент).

def new_func(named_arg, *args): # *args - идет после именованных параметров. Используется для любого кол-ва аргументов.
    print(named_arg)
    print(args) # Все аргументы доступны, как кортеж.

new_func(1, 2, 3, 4, 5) # Можно передавать любое кол-во аргументов.

def n_func(x, y, food="spam"): # Можно задать значение по умолчанию. Такое значение идет после именованных параметров.
    print(food)

n_func(1, 2)
n_func(3, 4, "egg") # Передача данных в food.

def k_func(x, y=7, *args, **kwargs): # kwargs - принимает несуществующие аргументы. Таков правильный порядок передачи аргументов.
    print(kwargs) # Доступно, как словарь, где имя переменной - ключ, а значение - значение аргумента.

k_func(2, 3, 4, 5, 6, a=7, b=8)


# try/except/finally/else

try: # Вызов инструкции try.
    print(7/0) # Проверка.
except ValueError: # Блок except (Можно написать несколько ошибок.)
    print("Откуда ты взял эту ошибку?") # Инструкция, которая выполняется в случае данной ошибки.
except: # Блок except (Можно вообще не писать ошибку. В таком случае инструкция выполняется в случае любой ошибки.)
    print("На ноль делить нельзя!") # Инструкция, которая выполняется в случае любой ошибки.
finally: # Вызов блока finally.
    print ("123") # Инструкция, которая будет выполнятся вне зависимости от того, была ли ошибка.


try:
    print(1)
except:
    print("Error")
else: # Работает только в том случае, если не было ошибки.
    print(2)

# raise

# raise ValueError | Выдаёт ошибку.

# assert

assert (5 - 5) == 0, "У кого-то проблемы с математикой." # Вызов блока assert(проверка, аргумент). Аргумент передаётся в ошибку.

# Работа с файлами.

myfile = open("Путь к файлу") # Открытия файла. Если файл находиться в текущей директории, то можно написать только его название.
file1 = open("Путь к файлу", "+") # Можно указать режим, в котором будет открыт файл.
"""
Режим	Обозначение
'r'	открытие на чтение (является значением по умолчанию).
'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x'	открытие на запись, если файла не существует, иначе исключение.
'a'	открытие на дозапись, информация добавляется в конец файла.
'b'	открытие в двоичном режиме.
't'	открытие в текстовом режиме (является значением по умолчанию).
'+'	открытие на чтение и запись
"""
text = myfile.read(16) # Получение содержимого из файла. Аргумент - число байтов. 
text = myfile.read() # Можно не указывать аргумент, в таком случае прочитает весь файл.
text = myfile.read(1) # Выводить будет пустую строку, ибо всё содержимое файла уже прочитано.
text = myfile.readlines() # Возвращает список, где каждый элемент является строкой файла [1\n, 2\n, 3]

file1.write("123") # Запись в файл.
bt = file1.write("Hello, file!") # Можно вернуть кол-во байт, записанных в файле.
print(bt) 

# Запись в текстовый файл идет исключительно в качестве строки. Чтобы записать число, необходимо его преобразовать в строку.

print(text) 
myfile.close() # Закрытие файла
file1.close() 

# none 
a = None # Пустое значение.

# Словари
# Содержит ключи и значения к ним. Каждый ключ, но НЕ значение, имеет свой индекс.

ages = {"Dave" : 24, "Mary" : 42, "John" : 58} # Создание словаря. Запись идет по принципу Ключ : Значение (Key:Value).
print(ages["Dave"]) # Вывод значения ключа.
ages["Dave"] = 32 # Изменение значения. Ключ НЕ меняется.
print("Dave" in ages) # Ищет ключ в словаре. True/False, в зависимости от результата.
print(ages.get("Dave")) # Ищет ключ в словаре. Возвращает значение или none, в зависимости от результата.
print(ages.get("Dave", "Name not found.")) # none можно заменить с помощью второго аргумента.
ages.pop("John") # Удаление элемента.
d = ages.copy() # Вовзращает копию словаря.
ages.clear() # Чистит словарь.
print(d.items()) # Возвращает ключи и их значения.
print(d.keys()) # Возвращает ключи словаря.
print(d.values()) # Возвращает значения словаря.

# Кортежи (Неизменяемые списки)

words = ("Spam", "eggs", "sausages") # Объявление кортежа.
print(words[0]) # Возвращает значение по индексу.
words = 1, 2, 3 # Можно создавать вообще без скобок.

# Распаковка кортежей.

numbers = (1, 2, 3)
a, b, c = numbers # Передача данных кортежа в переменные.

a, b = b, a # Таким же способом можно произвести замену переменных.

print(a)
print(b)
print(c)

numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers # c получает все значения, которые не вместились в переменные.

print(a)
print(b) # Является списком.
print(c)


# format

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2]) # Форматирование идет по порядку.
print(msg) # Вывод: Numbers: 4 5 6.
a = "{x}, {y}".format(x=5, y=12) # Форматирование.
print(a)

###################################################################################################################################

# Функциональное программирование в python.
    # Чистая функция.

def fun(x): # Пример чистой функции.
    return x + 5
# Чистой функцией является та, которая не имеет побочных эффектов и возвращает то значение, которая зависит ТОЛЬКО от аргументов.
fun(5)

    # Лямбда функция (Анонимная функция).

def func(f, arg):
    return f(arg)

func(lambda x: 2*x*x, 5) # Идет lambda, аргументы (получение), двоиточие, обрабатываемое выражение, и аргумент (отправка в функцию).
double = lambda x: x * 2
print(double(7)) # Можно присвоить переменную, и в таком случае будет использоваться, как обычная функция.

    # map

nums = [11, 22, 33, 44, 55] # Создаем сисок чисел.
result = list(map(fun, nums)) # map принимает как аргументы функцию и итерируемый объект (Например список), а после выполняет функцию.
print(result) # Вывод: [16, 27, 38, 49, 60]

    # filter

# возьмем список чисел из map
result = list(filter(lambda x:x % 2 == 0, nums)) # Берет в качестве аргумента функцию с логическим выражением и удаляет то, что false.

    # Генератор (yield)
txt = "1, 2, 3"
def gen(txt):
    txt = txt.split()
    for i in txt:
        yield i # Инструкция yield передаёт, что это генератор. Вместо return, только можно делать итерации, вызывая функцию повторно.

print (list(gen())) # В данном случае это не сильно видно, но мы производим итерации.

    # Декоратор (@)

def decor(func): # Функция, которая меняет вывод другой функции.
    def wrap():
        print("============")
        func() 
        print("============")
    return wrap

@decor # Равноцено строке: print_text = decor(print_text).
def print_text(): # Обычная функция.
    print("Hello world!") 

print_text() # Вызов готовой декорируемой функции.

    # Рекурсия.
    # Рекурсия - вызов функции самой себя.
    # Рекурсивная функция должна иметь базовый случай, чтобы не было бесконечной рекурсии и следственного RuntimeError.

def rec(x):
    if x == 1: # Базовый случай. Случай, в котором функция должна остановиться.
        return 1
    else:
        return x * rec(x-1) # Рекурсия.
print(rec(5))

###################################################################################################################################

# Множества. Тоже самое, что и списки с той разницеЙ, что в множествах значения не имеют дубликатов.
# Во множествах все значения не имеют индексов, но можно найти их кол-во через len().

nums = {1, 2, 1, 3, 4, "world"} # Объявление множества.
words = {"Hello", "world!"}
print(nums) # Вывод: 1, 2, 3, 4.
nums.add(-7) # Добавляет новый элемент.
nums.remove(-7) # Удаляет выбранный элемент.
nums.pop() # Удаляет произвольный элемент.
nums.clear() # Чистит множество.
print(nums | words) # Объединяет два множества.
print((nums | words) & words) # & - Возвращает совпадающие элементы.
print(nums - words) # Отнимает из первого множества второе.
print(nums ^ words) # Возвращает те элементы, которые не принадлежат сразу обоим множествам.


###################################################################################################################################

# Объектно-ориентированное программирование.

    # Классы

class Cat: # Объявление класса.
    def __init__(self, color, legs, name): # Создание метода (функции) с атрибутами color и legs.
        # Метод __init__ является главным методом любого класса и всегда стоит на первом месте. Называется конструктором класса.
        self.color = color # Создание атрибутов класса.
        self.legs = legs
        self.name = name
    
    def bark(self): # У всех методов первым аргументом всегда должен стоять self.
        print("Woof!")
        
felix = Cat("ginder", 4, "felix") # Объявляем экземпляры (объекты) класса с определенными атрибутами.
rover = Cat("dog-colored", 4, "rover")
stumpy = Cat("brown", 3, "stumpy")

print(felix.name) # Получение атрибута объекта.
felix.bark() # Обращение к методу экземпляра.

class Dog:
    legs = 4 # Можно создать атрибут класса.
    # Атрибуты класса являются общими для всех экзепляров класса.
    def __init__(self, color, name):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs) # Ссылка из экземпляра класса.
print(Dog.legs) # Ссылка из самого класса.

    # Суперклассы

class Product(): # Суперкласс или базовый класс.
    def __init__(self, price): 
        self.price = price # Это значение едино для всех производных классов.
    
class Food(Product): # Подклассы или производные классы.
    def food(self, edate): 
        self.edate = edate # Этот атрибут имеет только этот класс.

class Wear(Product):
    def wear(self, textile, price):
        self.textile = textile 
        self.price = price # Переопределение атрибута.

product = Wear(500) # Мы передаем сперва суперклассу значение атрибута.
product.textile = "Cotton" # Можем инициализировать другие атрибуты экземпляра.

# Можно использовать подкласс в качестве родительского для другого класса.

class A: # Супперкласс.
    def method(self):
        print("A method")
    
class B(A): # Наследуемый класс.
    def another_method(self):
        print("B method")
    
class C(B): # Наследуемый наследуемого (Родительским является A).
    def third_method(self):
        print("C method")
    
c = C()
c.method() # A method
c.another_method() # B method
c.third_method() # C method

    # Super

class x: # Суперкласс
    def spam(self):
        print(1)
    
class Y(x): # Подкласс
    def spam(self): 
        print(2)
        super().spam() # Вызов метода суперкласса.

Y().spam()

    # Магические методы

class Vector2D: # Создание класса.
    def __init__(self, x, y): # Инициализация атрибутов.
        self.x = x
        self.y = y

    def __add__(self, other): # Магический метод. Переопределяет оператор.
        return Vector2D(self.x + other.x, self.y + other.y) # self - левый операнд. # other - правый операнд.

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x) # Вывод: 8
print(result.y) # Вывод: 16

# Таким образом можно менять любые операторы в классе.
"""
__sub__ для -
__mul__ для *
__truediv__ для /
__floordiv__ для //
__mod__ для %
__pow__ для **
__and__ для &
__xor__ для ^
__or__ для |
__lt__ для <
__le__ для <=
__eq__ для ==
__ne__ для !=
__gt__ для >
__ge__ для >=
__len__ для len().
__getitem__ для индексации.
__setitem__ для присваивания значения индексированному элеметну.
__delitem__ для удаления индексированных элементов.
__iter__ для перебора объектов (например, в циклах for)
__contains__ для in
"""

    # del

a = 42 # Объявление переменной.
b = a # Объявление ссылки на переменную а.
c = [a] # Добавление ссылки на переменную а в список.

del a # Удаление переменной.
b = 100 # Переназначение b.
c[0] = -1 # Переназначение первого элемента списка.

    # @classmethod (Метод класса)

class MyClass: # Обычный класс.
    class_variable = "Hello, World!" # Атрибут класса.

    @classmethod # Декоратор, который объявляет следующий метод - методом класса.
    def class_method(cls): # cls - ссылка на класс, которая обязательно должна быть первой.
        print(cls.class_variable)

MyClass.class_method() # выведет "Hello, World!"

    # @staticmethod (Статический метод)
    # Такие методы объявляют тогда, когда не нужны дополнительные параметры, т.е. когда нужно выполнить какую-то операцию,
    # которая связана с классом, но не требует доступа к его атрибутам или методам экземпляра.

class MyClass: # Обычный класс.
    @staticmethod # Декоратор, который объявляет следующий метод - статическим методом.
    def static_method(x, y):
        return x + y

result = MyClass.static_method(3, 4) # result = 7

    # @property, getter, setter
    # Используется для моментального вычисления. Является обычной функцией. 
    # Используется тогда, когда идет обращение к переменной, и необходимо провести операцию над ней в момент обращения.

a = 42

class S_1:
    def __init__(self): # Инициализация приватной перменной.
        self.__age = None

    @age.setter # Сеттер.
    def age(self, age): 
        self.__age = age
    
    @property # Геттер.
    def age(self):
        return self.__age

age = S_1()
age.age = 16
print (age.age)


# __main__

def function():
    print("This is a module function") # Работает, если файл импортирован.

    if __name__ == "__main__":
        print("This is a script") # Работает, если файл запущен как исходник.

import test # Импорт другого файла.

test.test_func() # Обращение к функции в другом файле.

# Сборка пакетов

"""
При сборке пакетов структура каталого должна быглядеть примерно так:
SoloLearn/
    LICENSE.txt
    README.txt
    setup.py (exe)
    sololearn/
        __init__.py
        sololearn.py
        sololearn2.py

Где в SoloLearn обязательно должны быть файлы LICENSE.txt, README.txt, setup.py (exe), а в sololearn __init__.py
"""

# Стеки
# Работают по принципу Firs in, Last out (FILO). Используются, как пример, в буфере обмена.

class Stack:
    def __init__(self): # Инициализация стэка (списка).
        self.items = []  
  
    def is_empty(self): # Если стэк пустой.
        return self.items == []
  
    def push(self, item): # Добавление элемента в стэк.
        self.items.insert(0, item)
    
    def pop(self): # Удаление элемента из стэка.
        return self.items.pop(0)
    
    def print_stack(self): # Вывод стэка.
        print(self.items)
    
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()

# Очереди
# Работают по принципу First in, First out (FIFO). Используются, как пример, в колл-центре.

class Queue:
    def __init__(self): # Объявление очереди.
        self.items = []

    def is_empty(self): # Возврат пустой очереди.
        return self.items == []

    def enqueue(self, item): # Добавление нового элемента.
        self.items.insert(0, item)
 
    def dequeue(self): # Удаление элемента.
        return self.items.pop()

    def print_queue(self): # Вывод очереди.
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()

###################################################################################################################################

# Библиотека random

list_1 = list(range(20))

random.randrange(0, 10, 2) # Возвращает случайно выбранное число из последовательности (аргументы: начало, конец, шаг.).
num = random.randint(0, 10) # Возвращает случайное целое число (От и до).
random.choice(list_1) # Возвращает случайный элемент непустой последовательности.
random.shuffle(list_1, [rand]) # Перемешивает последовательность (изменяется сама последовательность). 
# Функция не работает с неизменяемыми объектами.

print(random.sample(list_1, num)) # Возвращает список случайных элементов длиной k из последовательности population.
random.random() # Возвращает случайное число от 0 до 1.
random.uniform(0, 10) # Возвращает случайное число с плавающей запятой.
random.triangular(0, 10) # Возвращает случайное число с плавающей запятой.




# Библиотека math

x = 5
z = 2 

list_1 = list(range(20))

math.ceil(x) # Округление вверх.
math.floor( x) # Округление вниз.
math.fabs(x) # Модуль x.
math.factorial(x) # Факториал числа x.
math.fmod(x, z) # Остаток от деления x на z.
math.frexp(x) # Возвращает мантиссу и экспоненту числа.
math.fsum(list_1) # Сумма всех членов последовательности. 
# Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.

math.isfinite(x) # Является ли x числом.
math.isinf(x) # Является ли x бесконечностью.
math.isnan(x) # Является ли x НЕ числом.
math.modf(x) # Возвращает дробную и целую часть числа x. Оба числа имеют тот же знак, что и x.
math.trunc(x) # Усекает значение x до целого.
math.exp(x) # Константа e в степени x.
math.log(x, ["""base"""]) # Логарифм x по основанию base. Если base не указан, вычисляется натуральный логарифм.
math.log10(x) # Логарифм x по основанию 10.
math.log2(x) # Логарифм x по основанию 2.
math.pow(x, z) # x в степени z.
math.sqrt(x) # Квадратный корень из x.
math.acos(x) # Арккосинус x. В радианах.
math.asin(x) # Арксинус x. В радианах.
math.atan(x) # Арктангенс x. В радианах.
math.atan2(z, x) # Арктангенс z/x. В радианах. С учетом четверти, в которой находится точка (x, z).
math.cos(x) # Косинус x (x указывается в радианах).
math.sin(x) # Синус x (x указывается в радианах).
math.tan(x) # Тангенс x (x указывается в радианах).
math.hypot(x, z) # Вычисляет гипотенузу треугольника с катетами x и z
math.degrees(x) # Конвертирует радианы в градусы.
math.radians(x) # Конвертирует градусы в радианы.
math.cosh(x) # Вычисляет гиперболический косинус.
math.sinh(x) # Вычисляет гиперболический синус.
math.tanh(x) # Вычисляет гиперболический тангенс.
math.acosh(x) # Вычисляет обратный гиперболический косинус.
math.asinh(x) # Вычисляет обратный гиперболический синус.
math.atanh(x) # Вычисляет обратный гиперболический тангенс.
math.pi # - pi = 3,1415926...
math.e # - e = 2,718281...




# Tkinter
from PIL import ImageTk, Image
import tkinter

from tkinter import ttk

icon = ImageTk.PhotoImage(file = "image.png") # Фотка.

def screen():
    window = tkinter.Tk() # Создание окна
    window.iconbitmap(default="favicon.ico") # Установка иконки в тайтле.
    window.title("Title") # Установка названия окна (тайтла).
    window.geometry("1280x1024") # Установка разрешения окна.
    window.config(background="black") # В конфиге могут быть различные настройки, например - настройка цвета фона.
    window.resizable(width=False, height=False) # Отключить изменение разрешения по длине и ширине.
    window.overrideredirect(True) # Отключить верхнюю панель приложения (панель приложения).
    window.attributes("-fullscreen", True) # Различные настройки. В данном случае - полноэкранный режим окна.
    window.iconphoto(False, icon) # Установка юзерной иконки.
    window.attributes("-alpha", 0.5) # Прозрачность окна.
    window.attributes("-toolwindow", True) # Убрать панель приложения за исключением заголовка и креста закрытия.

    return window

label_test = tkinter.Label()
label_test.pack()

label_test.winfo_class() # Возвращает класс виджета, например, для кнопки это класс TButton.

label_test.winfo_children() # Возвращает для текущего виджета список вложенных виджетов.

label_test.winfo_parent() # Возвращает родительский виджет.

label_test.winfo_toplevel() # Возвращает окно, которое содержит данный виджет.

label_test.winfo_width() # Текущая ширина виджета.
label_test.winfo_height() # Текущая высота виджета.

label_test.winfo_reqwidth() # Запрошенная виджетом ширина.
label_test.winfo_reqheight() # Запрошенная виджетом высота.

label_test.winfo_x()
label_test.winfo_y() # x и y координаты верхнего левого угла виджета относительно родительского элемента

label_test.winfo_rootx()
label_test.winfo_rooty() # x и y координаты верхнего левого угла виджета относительно экрана

label_test.winfo_viewable() # Указывает, отображается ли виджет или скрыт.

window = screen()
label_1 = tkinter.Label(text="Hello, Tkinter!") # Создание виджета.
label_1.pack() # Отображение виджета на окне. 
label_2 = tkinter.Label(text="Изменённые цвета.", bg="black", fg="white") # Изменение цветов.
label_2.pack()
label_3 = tkinter.Label(text="RGB colored", bg="#34A2FE") # Можно поставить RGB код цвета.
label_3.pack()

button_1 = tkinter.Button(text="Кнопка", width=25, height=5) # Создание кнопки. Имеет те же свойства, что и виджет.
button_1.pack()

btn = ttk.Button(text="Click Me", state=["disabled"]) # Отключение кнопки.
btn.bind("<Enter>", screen) # Обработка событий.
btn.pack()
"""
Activate: окно становится активным.

Deactivate: окно становится неактивным.

MouseWheel: прокрутка колеса мыши.

KeyPress: нажатие клавиши на клавиатуре.

KeyRelease: освобождение нажатой клавиши

ButtonPress: нажатие кнопки мыши.

ButtonRelease: освобождение кнопки мыши.

Motion: движение мыши.

Configure: изменение размера и положения виджета

Destroy: удаление виджета

FocusIn: получение фокуса

FocusOut: потеря фокуса.

Enter: указатель мыши вошел в пределы виджета.

Leave: указатель мыши покинул виджет.

"""

entry_1 = tkinter.Entry() # Создание однострочного текстового поля для ввода пользовательского текста.
entry_1.pack()
string = entry_1.get() # Получение данных из Entry.
entry_1.delete(0, tkinter.END) # Удаление всего текста в текстовом поле. (1-й аргумент - начало, 2-й аргумент - конец.)

entry_1.insert(0, "Вывод.") # Вывод текста в Entry. (1-й аргумент - индекс, 2-й аргумент - текст.)
entry_1.pack()

text_box = tkinter.Text()
text_box.pack()
a = text_box.get(1.0, tkinter.END) # Берет индексы начала и конец. Без хотя бы одного индекса будет выводить TypeError.
# Индексы беруться в формате 0.0, где первое число - строка, второе - символ. (2.3) - четвертый символ третьей строки.

text_box.delete(1.0, tkinter.END) # Также, как и с get.

text_box.insert(1.0, "Вывод.") # Вывод текста в Text. (1-й аргумент - индекс, 2-й аргумент - текст.)
text_box.insert(2.0, "Вывод.") # Будет Вывод.Вывод.
text_box.insert(3.0, "\nВывод снизу.") # Если надо перенести на следующую строку.

frame_a = tkinter.Frame() # Создание рамки.
frame_b = tkinter.Frame(relief=tkinter.SUNKEN, borderwidth=2) # Изменение стиля рамки.

frame_win = tkinter.Frame(
    frame_a, # Master.
    height=512, # Высота.
    width=640, # Ширина.
    background="black", # Цвет бэкграунда.
    borderwidth=5, # Размер выемки.
    highlightbackground="red", # Цвет выделения.
    highlightthickness=2 # Размер выделения.
    ) # Нужно сделать родительский label для размещения элементов в центре.
 
label_a = tkinter.Label(master=frame_a, text="I'm in Frame A" ) # Отправка виджета в рамку.
label_a.pack()
 
label_b = tkinter.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()
 
frame_a.pack()
frame_b.pack()

"""
FLAT - Нет рамки.
SUNKEN - Эффект углубления.
RAISED - Эффект выпуклости.
GROOVE - Эффект вырезания в текстуру, выемки.
RIDGE - Эффект выпуклой выемки.
"""

# Правила названий виджетов.

"""
Label - lbl;
Button - btn;
Entry - ent;
Text - txt;
Frame - frm.
"""





"""
fg/foreground - Цвет текста.
bg/background - Цвет фона.
height - Высота.
width - Ширина.
"""

# .pack

frame1 = tkinter.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tkinter.X) # Заливка по оси X, доступны значения Y и BOTH (Y - Вертикаль, BOTH - обе оси.)

frame2 = tkinter.Frame(master=window, height=20)
frame2.pack(fill=tkinter.BOTH, expand=True) # Для равномерного расширения.
# При расширении окна, все объекты будут равномерно увеличиваться.

label_side = tkinter.Label(height=2, width=2)
label_side.pack(side="top") # Расположение объекта.

# .place

frame = tkinter.Frame(master=window, width=150, height=150)
frame.pack()

label11 = tkinter.Label(master=frame, text="I'm at (0, 0)", bg="red")
label11.place(x=0, y=0) # Координаты по пикселям.
 
label22 = tkinter.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label22.place(x=75, y=75)

# .grid

label1 = tkinter.Label(text="1", bg="black", fg="white")
label2 = tkinter.Label(text="2", bg="black", fg="white")
label3 = tkinter.Label(text="3", bg="black", fg="white")
label4 = tkinter.Label(text="4", bg="black", fg="white")
 
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew") # Заполнение по горизонтали.
label3.grid(row=0, column=2, sticky="ns") # Заполнение по вертикали.
label4.grid(row=0, column=3, sticky="nsew") # Полное заполнение.

screen_width = window.winfo_screenwidth() # Размеры экрана (Ширина).
screen_height = window.winfo_screenheight() # Размеры экрана (Высота).

# Привязка переменных

def click_button():
    value = clicks.get() # Получить значение.
    clicks.set(value + 1) # Установить новое значение.

clicks = tkinter.IntVar(value=0) # Значение по умолчанию.

btn = ttk.Button(textvariable=clicks, command=click_button) # Привязка к переменной.
btn.pack(anchor=tkinter.CENTER, expand=1)

"""
Возможные получаемые значения:

StringVar
IntVar
BooleanVar
DoubleVar

"""

# checkbutton


enabled = tkinter.IntVar()


checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
checkbutton.pack(padx=6, pady=6, anchor="NW")

"""
command: ссылка на функцию, которая вызывается при нажатии на флажок

cursor: курсор при наведении на элемент

image: графическое изображение, отображаемое на элементе

offvalue: значение флажка в неотмеченном состоянии, по умолчанию равно 0

onvalue: значение флажка в отмеченном состоянии, по умолчанию равно 1

padding: отступы от текста до границы флажка

state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE

text: текст элемента

textvariable: привязанный к тексту объект StringVar

underline: индекс подчеркнутого символа в тексте флажка

variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка

width: ширина элемента
"""

# RadioButton

python_btn = ttk.Radiobutton(text="python")
python_btn.pack()

"""
command: ссылка на функцию, которая вызывается при нажатии на переключатель

cursor: курсор при наведении на виджет

image: графическое изображение, отображаемое виджетом

padding: отступы от содержимого до границы переключателя

state: состояние виджета, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE

text: текст виджета

textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя

underline: индекс подчеркнутого символа в тексте виджета

variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя

value: значение переключателя

width: ширина виджета
"""

# Listbox

languages_listbox = tkinter.Listbox()
languages_listbox.pack()

"""
listvariable: список элементов, которые добавляются в ListBox

bg: фоновый цвет

bd: толщина границы вокруг элемента

cursor: курсор при наведении на Listbox

font: настройки шрифта

fg: цвет текста

highlightcolor: цвет элемента, когда он получает фокус

highlightthickness: толщина границы элемента, когда он находится в фокусе

relief: устанавливает стиль элемента, по умолчанию имеет значение SUNKEN

selectbackground: фоновый цвет для выделенного элемента

selectmode: определяет, сколько элементов могут быть выделены. Может принимать следующие значения: BROWSE, SINGLE, MULTIPLE, EXTENDED. Например, если необходимо включить множественное выделение элементов, то можно использовать значения MULTIPLE или EXTENDED.

height: высота элемента в строках. По умолчанию отображает 10 строк

width: устанавливает ширину элемента в символах. По умолчанию ширина - 20 символов

xscrollcommand: задает горизонтальную прокрутку

yscrollcommand: устанавливает вертикальную прокрутку
"""




window.mainloop() # Отображение окна.

a = 0
if a:
    window.destroy() # Закрытие окна.


















# Регулярные выражения (библиотека re)

string = "spam"

if re.match(string, "spamspamspam"): # Ищет элемент в начале строки и возвращает True/False.
    print("match")

if re.search(string, "spamspamspam"): # Ищет элемент во всей строке (аналог in).
    print("Match")

print(re.findall(string, "spamspamspam")) # Возвращает список всех подстрок, которые совпадают.

print(re.finditer(string, "spamspamspam")) # Делает тоже самое, что и findall, только возвращает итератор вместо списка.

string = "da-da"

match = re.search("Di-ya, da-da-de-di-ya, da-da-de-di-ya, da-da-de-da") 
if match:
    print(match.group()) # Возвращает совпавшую строку.
    print(match.start()) # Возвращает начальную позицию совпавшей строки.
    print(match.end()) # Возвращает конечную позицию совпавшей строки.
    print(match.span()) # Возвращает начальну и конечную позицию совпавшей строки.

text = "My name is David. Hi, David!"
string = "David"
text = re.sub(string, "Amy", text, count=0) # Аналог replace, но можно еще добавить 4-й аргумент - кол-во заменяемых элементов.

    # Метасимволы

# ^ - Начало строки; $ - Конец строки

pattern = r"[A-Z]" # [] - Диапазон искомых символов (В данном случае весь алфавит, начиная с A до Z и только верхний регистр). 
# Можно ставить числа.

if re.search(pattern, "This is all quiet"):
    print("Match")

pattern = r"[^A-Z]" # ^ - Ставиться в начале диапазона. Ищет всё, что не совпадает с диапазоном.

pattern = r"egg(spam)*" # * - ищет в начале ноль или больше упоминаний символа.  

if re.match(pattern, "eggspamspamspam"):
    print("Match")

pattern = r"g+" # + - Ищет в начале один или больше упоминаний символа.

if re.match(pattern, "g") or re.match(pattern, "gggggg"):
    print("Match")

pattern = r"ice(-)?cream" # Ищет одно или ноль упоминаний символа в начале.

if re.match(pattern, "ice-cream") or re.match(pattern, "icecream"):
    print("Match")

pattern = r"9{1, 3}$" # {} - Ищет кол-во упоминаний в строке. Можно использовать Int переменные в место значений.
# Можно не ставить первое (Будет считать и ноль упоминаний) или последнее (Будет считать бесконечность упоминаний) значение.

if re.match(pattern, "999"):
    print("Match")

pattern = r"gr(a|e)y" # Или.

if re.match(pattern, "gray") or re.match(pattern, "grey"):
    print("Match")

pattern = r"(a+) \1" # Обращение к первой группе. () - группа.

if re.match(pattern, "word word"):
    print("Match")

text = "Hello, 123 World!"
digits = re.findall(r'\d+', text)  # Найти все последовательности цифр
print(digits)  # Вывод: ['123']

words = re.findall(r'\w+', text)  # Найти все "словесные" символы
print(words)  # Вывод: ['Hello', '123', 'World']

spaces = re.findall(r'\s+', text)  # Найти все пробельные символы
print(spaces)  # Вывод: [' ', ' ']





# itertools

l = []

for i in itertools.count(3): # Бесконечная прогрессия, начиная с заданного числа.
    l.append(i)
    if i >= 10:
        break

for i in itertools.cycle(l): # Бесконечно перебирает итерируемый объект.
  print(i)
  if i == l[-1]:
    break

print(list(itertools.repeat("spam", 10))) # Повторяет объект бесконечное или заданное кол-во раз.
print(itertools.takewhile(lambda x: x % 2 == 0)) # Возвращает значения, которые соответствуют проверке.
print(list(itertools.chain(l, l, l, l))) # Объединяет итерируемые объекты в один. 
print(itertools.accumulate(l)) # Прибавляет к каждому значению объекта предыдущие.



