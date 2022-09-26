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

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))
