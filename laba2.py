# '''Первая задача'''
# def palindrom(num):
#     num = abs(num)
#     list_num = list(str(num))
#     for i in range((int(len(list_num) / 2))):
#         #print(list_num[i], list_num[-i - 1], i)
#         if list_num[i] != list_num[-i - 1]:
#             return False
#     return True
#
#
# while True:
#     number = int(input('Введите число: '))
#     if number == -1:
#         print('До свидания')
#         break
#     else:
#         print(palindrom(number))

# '''Вторая задача'''
# def three_lists(list_num):
#     # a = [int(i) for i in list_num if int(i) % 2 == 0 and int(i) != 0]
#     # b = [int(i) for i in list_num if int(i) % 3 == 0 and int(i) != 0]
#     # c = [int(i) for i in list_num if int(i) % 5 == 0 and int(i) != 0]
#
#     # Если без повторов, то лучше кортеж
#     a = {int(i) for i in list_num if int(i) % 2 == 0 and int(i) != 0}
#     b = {int(i) for i in list_num if int(i) % 3 == 0 and int(i) != 0}
#     c = {int(i) for i in list_num if int(i) % 5 == 0 and int(i) != 0}
#
#     return a, b, c
#
#
#     #Для чисел: 1, 3, 5, 1, 4, 5, 1, 5, 2, 5, 6, 1, 5, 120, 4124, 51235, 125510, 20
#     #Результат: ({2, 4, 6, 125510, 20, 120, 4124}, {120, 3, 6}, {51235, 5, 125510, 20, 120})
#
# num = list(input('Введите числа через запятую:').split(', '))
# print(three_lists(num))

# '''Третья задача'''
# def obratnoe(num):
#     if abs(num) / 10 < 1:
#         return num
#     else:
#         result = ""
#         if num < 0:
#             num = abs(num)
#             result += '-'
#         num = list(str(num))
#         for i in range(len(num)):
#             if num[-i-1] == '0':
#                 continue
#             result += num[-i-1]
#     return result
#
# while True:
#     number = input('(stop - завершить выполнение программы)\nВведите число: ')
#     if number == 'stop':
#         break
#     print(obratnoe(int(number)))

# '''Четвёртая задача'''
#
# def root_N(num, deg, accur):
#     x0 = num / deg
#     x1 = (1 / deg) * ((deg - 1) * x0 + num / (x0 ** (deg - 1)))
#     while abs(x1 - x0) > accur:
#         x0 = x1
#         x1 = (1 / deg) * ((deg - 1) * x0 + num / (x0 ** (deg - 1)))
#
#     return str(x1)
#
#
# degree = int(input('Введите степень кореня: '))
# number = int(input('Введите число из которого нужно извлечь корень {}-ой степени: '.format(degree)))
# accuracy = int(input('Введите с какой точностью должен быть посчитан корень: '))
#
# accuracy = 1 / (10 ** accuracy)
# print('Результат: ' + root_N(number, degree, accuracy))


# '''Пятая задача'''
# def simple_or_not(num):
#     count = 2
#     while count <= num and num % count != 0:
#         count += 1
#     return count == num
#
# while True:
#     try:
#         number = int(input('Введите число от 0 до 100000: '))
#         if number == -1:
#             break
#         print(simple_or_not(number))
#     except ValueError:
#         print('Введите число!')

# '''Задача 7.1'''
#
# def cached(func):
#     cache = dict()
#     def wrapper(num):
#         if num in cache:
#             print('Такое уже посчитано, я верну оттуда, мне лень считать')
#             return cache[num]
#         else:
#             print('Придётся считать, ладно')
#             cache[num] = func(num)
#             return cache[num]
#     return wrapper
#
#
#
# @cached
# def function(k):
#     return 2 ** k
#
# while True:
#     number = int(input('Введите число степени двойки: '))
#     if number == 0:
#         break
#     print('Результат', function(number))

# '''Задача 7.2'''
#
# def cached(func):
#     cache = dict()
#     def wrapper(num, cnt):
#         if num in cache:
#             if cache[num][1] > 0:
#                 print('Такое уже посчитано, я верну оттуда, мне лень считать')
#                 cache[num][1] -= 1
#                 return cache[num][0]
#             else:
#                 print('Придётся считать, ладно')
#                 temp = [func(num, cnt), cnt]
#                 cache[num] = temp
#                 return cache[num][0]
#         else:
#             print('Придётся считать, ладно')
#             temp = [func(num, cnt), cnt]
#             cache[num] = temp
#             return cache[num][0] # можно было бы вынести отдельно эти два else
#     return wrapper
#
#
# @cached
# def function(n, c):
#     return 2 ** n
#
# while True:
#     number = int(input('Введите число степени двойки: '))
#     count = int(input('Введите количество посчитанных значений: '))
#     if number == 0:
#         break
#     print('Результат', function(number, count))




