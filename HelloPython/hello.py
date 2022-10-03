from importlib.resources import path
from multiprocessing.sharedctypes import Value

                                   # АРИФМИТИЧЕСКИЕ ОПЕРАЦИИ 

# # print('hello world')
# # типы данных и переменных 
# # int, float, boolean, str, list, None

# a = 123 
# b = 1.23 
# # print(type(a))
# # print(type(b))

# value = None
# value = 12345
# # print(type(value))

# s = 'hello world'
# print(s) # Вывод строки
# print(a)
# print(b)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a,b,s)) # или print(f'{a} - {b} - {s}')

# # порядок переменных можно менять 
# # print('{0} - {1} - {2}'.format(a,b,s))
# #                                0 1 2


# list = [1,2,3] # Массив данных 
# print(list)

# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a,b)

# a = 2
# b = 8
# c = a * b
# print(c)

                                          # ЛОГИЧЕСКИЕ ОПЕРАЦИИ 

# >, >=, <, <=, ==, !=
# not, and, or, - не путать с &, |, ^
# is, is not, in, not in
# gen 

# a = 1 < 4 and 5 > 2
# print(a)

# a = int(input('Ведите число '))
# b = int(input('Ведите число '))
# if a > b: 
#     print(a)
# else:
#     print(b)    

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Артур':
#     print('Артур - держись')
# else:
#     print('Привет, ', username)

                                  # ЦИКЛ while 
# a = 23
# b = 0
# while a != 0:
#     b = b * 10 + (a % 10)
#     a //= 10
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(b)

                                  # ЦИКЛ for

# for i in 1,2,3,4,5:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

                                       # ФУНКЦИИ

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))

                                         #ЛЕКЦИЯ 2 данные функции и модули
                                         # первый вариант
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') # ('file.txt' - путь к файлу, 'a' - мод )
# data.writelines(colors) # разделителей не будет
# data.write( '\n LINE 1\n')
# data.write( 'LINE 2\n')
# data.close()
                                        # второй вариант


# with open('file.txt', 'w') as data:
#     data.write('lene 1\n')
#     data.write('lene 2\n')
                                        # Третий вариант

# # path = 'file.txt'
# # data = open(path, 'r')
# # for line in data:
# #     print(line)
# # data.close()
# exit()
                                        # ФУНКЦИИ импорт
# import hello as h
# print(h.f(1))

                                        # ФУНЦИИ умножения строк

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))   # ! ! ! ! !
# print(new_string('!'))    # ! ! ! 
# print(new_string('4'))    # 12

                                        # функция 

# def concatenatio (*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio('1', '2', '3', '4')) # TypeError: .....


                                        # РЕКУРСИЯ 

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib (n-1) + fib(n-2)

# list = []
# for e in range (1, 10):
#     list.append(fib(e))
# print(list) # 1, 1, 2, 3, 5, 8, 13, 21, 34

                                        # КОРТЕЖИ - не изменяемый список

# a = (3, 4)
# print(a)
# print(a[0])

                                        # СЛОВАРИ


# dictionary = {}
# dictionary = \
# {
#     'up': 'верх',
#     'left': 'лево',
#     'down': 'вниз',
#     'right': 'право'
# }
# print(dictionary) # 'up': 'верх','left': 'лево','down': 'вниз','right': 'право'
# print(dictionary['left']) 

                        # обращение ключи (up left down right)
# for k in dictionary.keys():
#     print(k)
                        # обращение к значению (верх лево вниз право)
# for k in dictionary.values():
#      print(k)

                                        # Списки
# list1 = [1,2,3,4,5]
# list2 = list1
# print(list1.pop()) - удаление элимента
# print(list1.insert()) - вставить элимента
# print(list1.append()) - добавление в конец
# for e in list1:
#     print(e)

# print()


# for e in list2:
#     print(e)




