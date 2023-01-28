# name_first = "Elena"  # переменная для имени
# print("Hello,", name_first)
# age = 20
# print(age)

# a = 5
# print(a)
# print(type(a))
# b = "6"
# print(type(b))
# print(b)
# print(str(a) + b)  # 56  11

# a = 4
# b = 5
# print(b)
# print(id(b))
# # print(id(b))
# a = b
# print(a)
# print(id(a))

# a = b = c = 5
# a, b, c = 2, "Hello", 4.5
# print(a, b, c)
#
# PI = 3.14
# print(PI)

# a = True
# print(type(a))

# print("строка \
# символов")
# print('строка '
#       'символов')

# print("Документ \r\"file.py\" находится      по \t\tзаданному пути: \nD:\\python\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)

# print(546545415145486484864864654)
# print(5.46545415145486484864864654)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(6 / 4)
# print(6 // 4)
# print(6.7 % 4)

# a = 5
# b = 7
# c = 3
# sum1 = a + b + c
# print('Сумма:', sum1)
# print('Произведение:', a * b * c)
# print('Среднее арифметическое:', sum1 / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12
#
# num *= 4  # num = num * 4
# print(num)  # 48

# num = 4321
# print(num)
# a = num % 10
# print("a =", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b =", b)
# num = num // 10
# print(num)
# c = num % 10
# print("c =", c)
# num = num // 10
# print(num)
# d = num % 10
# print("d =", d)
# print(a, b, c, d)
# print(a * 1000 + b * 100 + c * 10 + d)


# num = 9753  # 4
# print(num)
# res = num % 10 * 1000  # 1000
# num = num // 10
# res += num % 10 * 100  # 1200 = 1000 + 200
# num = num // 10
# res += num % 10 * 10  # 1230 = 1200 + 30
# num = num // 10
# res += num % 10  # 1234 = 1200 + 4
# print("res =", res)


# Задать пятизначное число (12345)
# Найти произведение цифр числа
# Найти среднее арифметическое цифр числа

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# Функции явного преобразования типов:
# int()
# str()
# float()
# bool()

# num1 = "2"
# num2 = 3.5
# res = int(num1) + num2
# print(res)
# a = 3.891
# a = round(a, 2)
# print(a)
# print(type(a))


# num1 = "5.2"
# num2 = 10
# c = float(num1) + num2
# print(bool(c))
# print(bool(0))

# name = "Виктор"
# age = 26
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end=" ")
# # print()
# print("Я учу Python.")

# name = input("Введите имя: ")
# print("Вас зовут", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# b1 = True
# b2 = False
#
# print(b1 + 5)  # True (1) + 5 = 6
# print(int(b1))
# print(b2 * 5)  # False (0) * 5 = 0
# print(int(b2))


# print(bool("Python"))
# print(bool(""))  # False
# print(bool(-9))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
#
# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 9 - 2)
# print(7 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(6 <= 8)
# print("привет" > "Привет")

# print(2 < 4 < 9)  # True && True = True
# print(3 * 3 <= 7 >= 2)  # False && True = False
# print(2 * 5 > 7 >= 4 + 3)  # True && True = True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True = True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False = False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True = True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False = True

# print(not 9 - 5)
# print(not 9 - 9)
# a = 0
# print(not a)


# cnt = 15
# if cnt < 10:  # False
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 25
# b = 15
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")

# a = input('a: ')
# b = input('b: ')
# c = input('c: ')
# if a == b == c:
#     print('Равносторонний')
# elif a == b or b == c or a == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     print("Время года - ", end="")
#     if 3 <= month <= 5:
#         print("Весна")
#     if 6 <= month <= 8:
#         print("Лето")
#     if 9 <= month <= 11:
#         print("Осень")
#     if month == 12 or month == 1 or month == 2:
#         print("Зима")
# else:
#     print("Такого месяца не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
#     # if n == 1:
#     #     print(n, "ворона")
#     # if 2 <= n <= 4:
#     #     print(n, "вороны")
#     # if 5 <= n <= 9 or n == 0:
#     #     print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# a = int(input("Введите число от 1 до 99: "))  # 23
# kop = a
# if 1 <= a <= 99:
#     if 11 <= a <= 14:
#         print(a, "копеек")
#     else:
#         kop = kop % 10  # 3
#         print(a, end=" ")
#         if kop == 1:
#             print("копейка")
#         elif 2 <= kop <= 4:
#             print("копейки")
#         else:
#             print("копеек")
# else:
#     print("Некорректное число")


# a = int(input("Введите число от 1 до 99: "))  # 23
# kop = a
#
# if 11 <= a <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 10 or 15 <= a <= 99:
#     kop = kop % 10  # 3
#     print(a, end=" ")
#     if kop == 1:
#         print("копейка")
#     elif 2 <= kop <= 4:
#         print("копейки")
#     else:
#         print("копеек")
# else:
#     print("Некорректное число")

# a = int(input("Введите число от 1 до 99: "))  # 23
# kop = a
#
# if 11 <= a <= 14:
#     print(a, "копеек")
# elif a <= 0 or a >= 100:
#     print("Некорректное число")
# else:
#     kop = kop % 10  # 3
#     print(a, end=" ")
#     if kop == 1:
#         print("копейка")
#     elif 2 <= kop <= 4:
#         print("копейки")
#     else:
#         print("копеек")

# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_3
#     case шаблон_n:
#         действие_n
#     case _:
#         действие по умолчанию

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case 'moderator':
#         print("Модератор")
#     case _:
#         print("Пароль не верен")


# day = 'среда'
# time = 14
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

#
# a, b = 20, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")


# a, b = 20, 0
# print("на ноль делить нельзя" if b == 0 else a / b)

# try ... except

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Нельзя вводить стоки")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить стоки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так")
# else:
#     print("Все нормально. Ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
#
# print("\nКод далее")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)  # n = 5
#     m = int(m)  # m = 'fff'
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)
#
#
# try:
#     n = input("Введите первое число: ")
#     m = input("Введите второе число: ")
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)


# a = input('Введите первое значение')
# b = input('Введите второе занчение')
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)


# Циклы
# i = 0
# while i <= 100:
#     print("i =", i)
#     i = i + 10  # i += 10

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1  # i += 10


# i = 2
# while i <= 20:
#     print("i = ", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите количество символов: "))
# # i = 0
# # while i < n:
# #     print("*", end="")
# #     i += 1
# while n > 0:
#     print("*", end="")
#     n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     print(a, end=" ")
#     if a % 2:  # 3 % 2 = 1
#         res += a  # res = res + a
#     a += 1
# print("\n", res)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if not n > 0:
#         break

# res = 1
#
# while True:
#     n = int(input("Введите целое число: "))
#     if n == 0:
#         break
#     res *= n
#
# print(res)

# i = 0
# while i < 3:
#     if i == 2:
#         break
#     # if i == 2:
#     #     i = "a" + i
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
#
# print("За циклом")


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# j = 0
# while j < 5:
#     print(" " * j, "*")
#     j += 1
# print()
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(end=" ")
#         j += 1
#     print("*")
#     i += 1

# for element in collection:
#     тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green', 20, 0.3:
#     print(color)

# print(range(9))

# range(start, stop, step)

# for i in range(9, -1, -1):
#     print(i, end=" ")
#
# print()
# i = 0
# while i < -1:
#     print(i, end=" ")
#     i += 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 101, 11):
#     print(i, end=" ")
# print()
# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done!')

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# symbol = input("Введите символ: ")
# for i in range(h):
#     for j in range(w):
#         print(symbol, end="")
#     print()

# w = 16
# h = 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# w = [i * 2 for i in "Hello"]
# print(w)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)
# nums = [8, 3, 9, 4, 1, [2, 5, 6], "H", 2.6, True]
# print(nums)
# print(type(nums))

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(nums[1])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(len(nums))

# s = [5] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
#
# c = s + b
# print(c)


# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(n2)
# if n == n2:
#     print("списки равны")
# else:
#     print("списки разные")

# генератор списков
# n = 5
# a = [i for i in range(1, n + 1)]
#
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input('-> ')
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]  # range(4)
# print(a)

# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, ":", a[i])
# print()
#
# for i in a:
#     print(i)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# n = list(range(21, 41))
# print(n)

# lst = [i for i in range(21, 41)]
# print(lst)
# a = 0
# b = 0
# for i in lst:
#     if i % 2 == 0:
#         a += 1
#     else:
#         b += i
# print('Количество четных элементов списка:', a, '\nСумма нечетных элементов:', b)


# sum1 = 0
# sum2 = 0
# n = list(range(21, 41))
# print(n)
# for i in n:
#     if i % 2 == 0:
#         sum1 += 1
#     if i % 2:
#         sum2 += i
# print(sum1)
# print(sum2)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#     s += a[i]
# print(s / k)

# a = [6, 3, 0, 8, 2]
# a[0], a[1] = a[1], a[0]
# print(a)

# срез
# список[start:stop:step]
# список[start:stop]
# список[:]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[4:1:-1])
# b = a[2:20]
# print(b)

# [1, 2, 3, 4, 5, 6, 7]
# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[-3:1:-1])
# print(s[2:5])
#
# a = "Hello"
# print(a[::-1])
#
# print(list(a))

# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:5]
# print(a)

# Методы списка

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.append(9)  # добавляет элемент в конец списка
# print(a)
# a.extend([5, 6, 7])  # добавляет список элементов в конец существующего списка
# print(a)
# a.extend("add")
# print(a)

# b = []
# a = []
# a.extend([i**2 for i in range(1, 11)])
# [a.extend([i**2]) for i in range(1, 11)]
# for i in range(1, 11):
#     a.extend([i ** 2])
# print(a)


# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2, 100)  # добавляет элемент списка (второй параметр - добавляемое значение) в определенное место (первый
# # параметр - задает
# # индекс),
# print(a)
# a.insert(0, 200)
# print(a)
# a.insert(len(a), 300)
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делиться на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# # if len(b) > len(a):
# #     for i in range(len(a)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):
# #         c.append(b[i])
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(b), len(a)):
# #         c.append(a[i])
# print(c)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.remove(2)  # удаляет первый по найденному совпадению элемент из списка (по значению)
# print(a)
# last = a.pop()  # удаляет последний элемент из списка (без параметров) и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(-2)  # удаление элемента по индексу
# print(a)
# print(second)
# a.clear()  # очищает список
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# k = int(input("Введите индекс:\nk = "))
# a.pop(k)
# print(a)


# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(8)  # считает количество заданных значений в списке
# print(num)
#
# b = 8
# if b in a:
#     ind = a.index(b, 4, -1)  # возвращает положение первого индекса по заданному значению
#     print(ind)


# c = [1, 2, 3]
# d = c.copy()  # возвращает копию списка
# print("c =", c)
# print("d =", d)
# c.append(4)
# d.insert(0, 100)
# print("c =", c)
# print("d =", d)

# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# a.reverse()  # перестроили элементы списка в обратном порядке
# print(a)
#
# a.sort()  # отсортировали список по возрастанию
# print(a)

# a.sort(reverse=True)  # отсортировали список по убыванию
# print(a)

# b = sorted(a, reverse=True)
# print("b =", b)
# print("a =", a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(reverse=True, key=len)
# print(s)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(6, 15, 2))


# import random as r
#
# print(r.randint(0, 5))
# print(r.randrange(6, 15, 2))


# from random import randint, randrange as rr
#
# print(randint(0, 5))
# print(rr(6, 15, 2))


# from random import *
#
# print(randint(0, 5))
# print(randrange(6, 15, 2))
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))
#
# # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# city_list = 'Новосибирск'
# print(choice(city_list))
# print(choices(city_list, k=3))
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=3))
# shuffle(s)
# print(s)


# from random import randint
#
# mas = [randint(0, 20) for i in range(5)]
# print(mas)

# Функции агрегирования

# lst = [7, 12, 20, 18, 9]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
#
# print("(" < ")")  # 101 == 97


from random import randint

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)

# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
#
# min_1 = min(lst)
# print(min_1)
#
# ind = lst.index(min_1)
#
# # del lst[:ind]
# # print(lst)
# print(lst[ind:])

# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("!!! Список пустой")

# print(bool(lst))

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
#
# print("Первый список:", a)
# print("Второй список:", b)

# c = a + b
# print("Третий список:", c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print("Элементы обоих списков без повторений:", c)

# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# k = int(input("Размер списка: "))  # 5
# s = []
# # while len(s) < k:  # len(s) != k
# #     w = randint(0, k-1)
# #     if w not in s:
# #         s.append(w)
# # print(s)
#
# for i in range(100):
#     w = randint(0, k-1)
#     if w not in s:
#         s.append(w)
# print(s)

# m = [
#     [1, 2, 3, 4, 77, 99],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, 4]
# ]
# # print(len(m))
# # print(m)
# # # print(m[1][2])
# # for row in range(len(m)):
# #     for col in range(len(m[row])):
# #         print(m[row][col], end="\t\t")
# #     print()
# # print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()
#
# for row in m:
#     for x in row:
#         print(x, end='\t\t')
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x ** 2, end='\t\t')
#     print()

# matrix = [[0 for x in range(5)] for y in range(3)]
#
# # matrix = []
# #
# # for y in range(3):
# #     new_row = []  # [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
# #     for x in range(5):
# #         new_row.append(0)
# #     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)


# matrix = [[randint(1, 30) for x in range(5)] for y in range(3)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#     print()

# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# s = 0
# for row in matrix:
#     for j in row:
#         print(j, end="\t\t")
#         if j < 0:
#             s += 1
#     print()
# print("Количество отрицательных элементов: ", s)

# n = int(input("n = "))
# m = [[randint(0, 100) for x in range(n)] for y in range(n)]
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
#
# t = m[0][0]
# for k in range(n):
#     if t > m[k][k]:
#         t = m[k][k]
# print(t)

# https://github.com/

# print("Hello")

# print("Проверка репозитория")


print("Вносим изменения в слонированный проект")


print("Hello")






