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


# from random import randint

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


# print("Вносим изменения в слонированный проект")
#
#
# print("Hello")

# def summa(a, b, c):
#     sm = a + b + c
#     avg = sm / 3
#     return avg
#
#
# q = summa(1, 2, 3)  # q = 2.0
# print(q ** 2)
# # summa(4, 6, 8)  # e = 6.2
# # # print(e)
# # summa(10, 8, 6)
# print(q)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# print(id(lt1))
# print(id(lt2))
#
# a = 2
# b = 2
# print(a == b)
# print(a is b)
#
# print(id(a))
# print(id(b))


# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# lt1[1] = "Hello"
# print(lt1)
# print(id(lt1))


# s = "Hello"
# print(id(s))
# s += 'World'  # s = s + "World"
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1  # a = a + 1
# print(a)
# print(id(a))


# s = "Hello"
# print(s[1])
# s[1] = 't'
# print(s)

# def add_number(n):
#     print("n", n, "=", id(n))
#     n = n + [4]  # n += [4]  ; n = [1, 2, 3] + [4]
#     print("n1", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print("x:", x, "=", id(x))
# add_number(x)
# print("x:", x, "=", id(x))


# Кортеж (tuple)

# lst = [1, 2, 3]
# tpl = (1, 2, 3)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# print(type(tpl))

# a = (5, 2)
# print(a)
# print(type(a))
# b = tuple("Hello")
# print(b)
# print(type(b))


# tpl = (1, 2, 3, 4, 5, 6, 7)
# print(tpl)
# print(tpl[2])
# # tpl[2] = 10
# print(tpl[1:3])

# from random import randint

# s = tuple(input("-> ") for i in range(3))
# s = tuple(randint(1, 30) for i in range(10))
# print(s)
# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# # print(t1 * 2)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# # if 'l' in t3:
# #     print(t3.index('l'))
# # else:
# #     print("Такого символа нет")
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:  # tpl.count(el) == 1
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def range_tuple(num1, num2):
#     return tuple(randint(num1, num2) for _ in range(10))
#
#
# tpl1 = range_tuple(0, 5)
# tpl2 = range_tuple(-5, 0)
# print(tpl1)
# print(tpl2)

# def tpl(n1, n2):
#     return tuple(randint(n1, n2) for i in range(10))
#
#
# tl1 = tpl(0, 5)
# tl2 = tpl(-5, 0)
# print(tl1)
# print(tl2)
# tl3 = tl1 + tl2
# print(tl3)
# print(tl3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)

# t = (1, 2, 3)
# del t
# print(t)


# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst = list(tpl)
# print(type(lst))
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "\nНаселение:", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, " (население: ", city_population, ")", sep="")


# Множество (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))
# lst = ["banana", "apple", "orange", "banana", "apple"]
# a = set(lst)
# a = set("Hello")
# print(type(a))
# print(a)


# s = {x * x for x in range(10)}
# print(s)

# def to_set(a):
#     x = set(a)
#     n = len(x)
#     return x, n
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', "green", "blue"}
# # print("green1" not in t)
# for i in t:
#     print(i)

# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in lst if 'a' not in i}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'}
# print(a)
#
# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# users = {"Tom", "Alice", "Bob"}
# users.add("Ann")
# print(users)
# user = "Tom"
# if user in users:
#     users.remove(user)
# print(users)

# users.discard("Rob")
# print(users)

# users.pop()
# print(users)

# users.clear()
# print(users)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# c = a ^ b
# # a |= b
# # a &= b
# print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# a = set(input())
# b = set(input())
# c = a & b
# print(c)

# str1 = "Hello"
# str2 = "How are you"
# # s1 = set(str1)
# # s2 = set(str2)
# # s = s1 | s2
# s3 = set(str1) & set(str2)
# for i in s3:
#     print(i, end=" ")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a < b)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one = drawing ^ music
# print(one)
#
# both = drawing & music
# print(both)
#
# drawing = drawing - both
# print(drawing)

# frozenset (замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset("hello")
# print(a)


# Словарь (dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(s[1])
# print(d["two"])

# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)

# d = {"one": 1, "two": 2, "three": 3}
# print(list(d))
# lst = ['one', 'two', 'three']
# # print(dict(lst))
#
# a = [
#     ['one', 1],
#     ('two', 2),
#     ('three', 3),
# ]
# print(dict(a))

# d = {"one": 45, 0: "text", (1, 2.3): 'Кортеж', 43: [2, 3, 6, 7], True: False}
# print(d[0][1])
# from random import randint
# # d = {i: i ** 2 for i in range(2, 7)}
# d = {input("n = "): input("-> ") for i in range(3)}
# # d = {str(i) + ")": randint(1, 100) for i in range(1, 11)}
# print(d)


# d = {"one": 1, "two": 2, "three": 3}
# print(len(d))
# d['two'] = 200
# d['one'] += 100
# print(d)

# for key in d:
#     print(key, ":", d[key])
# key = "two"
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
# print(d)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой ключ исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3430', 5, 6400],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         qty = int(input("Количество: "))
#         goods[n][1] += qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d['b'] = 5
# d2['e'] = 7
# print("D =", d)
# print("D2 =", d2)


# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['b'])
# # value = d.get('b1', 'Такого ключа нет')
# # print(value)
# # print(d.keys())  # ключи
# # print(d.values())  # значения
# # print(d.items())  # ключи + значения
# #
# # for k, v in d.items():
# #     print(k, "->", v)
# #
# # print(list(d.items()))
# print(d)
# item = d.pop('e', 5)
# item = d.popitem()
# item = d.setdefault('c', 100)  # устанавливает значение по умолчанию
# print(item)
# d.clear()
# d.update([('r', 7), ('c', 6)])
# d.update({'r': 7, 'c': 6})
# print(d)
# print(dict([('r', 7), ('c', 6)]))


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}

# z = x.copy()
# z.update(y)
# z = x | y
# print(z)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# # print(d)
# # print(new_d)
# d['location'] = d.pop('city')
# print(d)


# a = {
#     'first': {
#         1: "one",
#         2: "two",
#         3: "three",
#     },
#     'second': {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])


# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({key: value for key, value in d.items() if value <= 2})

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d['two'] = []
#         s = i  # 'two'
#     else:
#         d[s].append(i)  # d['two'].append(10)
#
# print(d)  # {'one': [1,2,3], 'two': [10, 20]}

# zip()
# a = [12, 1, 2]
# b = ['Dec', "Jan", "Feb", 3]
# c = [4.0, 8.5, 4.9]
# d = dict(zip(a, b))
# f = {k: v for k, v in zip(b, a)}
# print(d)
# print(f)

# f = zip(a, b, c)
# print(list(f))

# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'email': 'irina@gmail.com', 'job': 'Manager'}
# dict_three = {'name': 'Irina', 'email': 'irina@gmail.com', 'job': 'Manager'}
# for (k1, v1), (k2, v2), (k3, v3) in zip(dict_one.items(), dict_two.items(), dict_three.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#     print(k3, "->", v3)

# a = {'b': 1, 'a': 4, 'd': 2, 'c': 3}
# d = list(a.items())
# print(d)
# n, m = zip(*d)
# print(n)
# print(m)
# c = list(zip(n, m))
# print(c)
# c.sort()
# print(c)
#
# c = list(zip(m, n))
# print(c)
# c.sort()
# print(c)
# print(dict(c))
# c = {v: k for k, v in c}
# print(c)

# month = ['January', "February", "March"]
# total_sales = [52000.00, 51000.00, 48000]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)

# one = {'a': 1, 'b': 2, 'c': 55}
# two = {'c': 3, 'd': 4}
# print({**two, **one})  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# data = ["red", "green", "blue"]
# ind = 1
# for i in data:
#     print(ind, i)
#     ind += 1
# print()
# for n, i in enumerate(data, 1):
#     print(n, i)


# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
#
# for i, (j, v) in enumerate(dict_one.items(), 1):
#     print(i, j, "->", v)
# print()
#
# for i, v in enumerate(dict_one.values(), 1):
#     print(i, "->", v)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 3))
# print(func(5, 3, 2, 7))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 4, 5))

# def to_dict(*args):
#     return {k: k for k in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def qew(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     return [x for x in args if x < avg]
#
#
# print(qew(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(qew(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 7, 8, 9, 4))

# def print_scores(student, *scores):
#     print("\nStudent Name:", student)
#     # for score in scores:  scores = (10, 95, 88, 92, 99)
#     #     print(score, end=" ")
#     print(*scores)  # *scores = 10 95 88 92 99
#
#
# print_scores("Jonathan", 10, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33, 56)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

#
# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name='Irina', surname="Sharma", age=22)
# intro(name='Igor', surname="Wood", email="igor@gmail.com", age=25, phone=9876543210)


# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     # global my_dict
#     # my_dict = my_dict | kwargs
#     # return my_dict
#     my_dict.update(kwargs)
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyer_color='gray')
# print(my_dict)

# def func1(*args):
#     print(args[0])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func1(5)

# def func(first, *args, c=100, **kwargs):
#     return args, c, first, kwargs
#
#
# print(func(5, 4, 8, 9, 7, a=6, b=2, c=10))


# Области видимости (scope)

# name = 'Tom'
# surname = ""
#
#
# def hi():
#     global name, surname
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print(surname)
# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5
# x = 3
#
#
# def add_two(a):
#     # x = 2
#
#     def add_some():
#         # x = 5
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# min = 5
# print(min)
# a = [4, 5, 7, 8, 9]
# print(a)
# print(max(a))
# print(min(a))

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)  # 55

# x = 2
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()

# def outer(a1, a2, b1, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # return a, b
#
#     inner()
#     # a, b = x, y
#     return [a, b]
#
#
# print(outer(2, 3, 5, 7))  # [5, 12]

# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#
#
# rect_paral_square(2, 4, 6)
# print(s)
# rect_paral_square(5, 8, 2)
# print(s)
# rect_paral_square(1, 6, 8)
# print(s)


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     # s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(11))
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

#
# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res2()
# res1()
#
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(80, 101)
# B = make(70, 80)
# C = make(50, 70)
# D = make(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# Анонимные функции (lambda)

# def name(x, y):
#     return x + y
#
#
# print(name(3, 5))
# print((lambda x, y: x + y)(1, 2))
# print()
# (lambda x, y: print(x + y))(1, 2)

# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x=2, y=5: x + y)())
#
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda *args: args)(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)(5))


# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# add2 = outer1(5)
# print(add2(10))
#
# outer2 = lambda n: lambda x: x + n
# add3 = outer2(5)
# print(add3(10))
#
# print((lambda n: (lambda x: x + n))(5)(10))
#
# print((lambda n: lambda x: lambda z: z + n + x)(2)(4)(6))


# def func(i):
#     return i[1]
#
#
# d = {'d': 10, 'b': 15, 'c': 4}
# # a = sorted(d)
# # print(a)
# list_d = list(d.items())
# print(list_d)
# # list_d.sort(key=lambda i: i[1])
# list_d.sort(key=func)
# print(list_d)
# print(dict(list_d))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# # 12, 3
# print(a[3](12, 3))


# a = {'one': lambda x: x - 1, 'two': lambda x: x * (-1), 'three': lambda x: x ** 1}
#
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда")
# }
#
# d[2]()

# print((lambda a, b: a if a > b else b)(5, 13))

# print((lambda a, b, c: a if a < b and a < c else b if b < c and b < a else c)(15, 16, 13))


# map(func, iterables), filter(func, iterables)  -  циклы


# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a1)


# t = (2.88, -1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# t3 = tuple(map(int, t))
# print(t3)


# areas = [3.564897, 7.4512368, 8.412578, 4.456712, 5.456782, 2.321456]
#
# print(list(map(round, areas, [2, 5, 2, 3, 6, 1])))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))
#
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))  # ([1, 2, 3], [4, 5, 6])
#
#
# a = l1, l2
# print(a)


# t = ('abcd', 'abc', 'cdrfg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# from random import randint
#
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print("[10; 20] = ", list(filter(lambda s: 10 <= s <= 20, lst)))


# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))  # [0,1,2,3,4,5,6,7,8,9] => [1,3,5,7,9]


# Декораторы
# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(type(test))
# print(test())

# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 50)
#         func()
#         print('*' * 50)
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Тело функции 'func_test'")
#
#
# @my_decorator
# def hello():
#     print('Hello, I am func "hello"')
#
#
# func_test()
# hello()
# test = my_decorator(func_test)
# test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут:", name, surname)
#
#
# print_full_name("Ирина", "Леонова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# print(int('19'))
# print(int('19.5'))  # ValueError

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0B10010)
# print(0O22)
# print(0X12)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("Py1" in e)

# s = "Hello"
# print(s[1])
# print(s[-5])
# print(s[1:4])
# print(s[::-1])

# s = 'python'  # pytton
# # s[3] = "t"
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_to_str(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\file\\"[:-1])
# print(r"C:\folder\file" + "\\")
# print("C:\\folder\\file\\")


# name = "Дмитрий"
# age = 25
#
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print(f"Меня зовут {name}. Мне {age} лет")

# from geometry import pi
#
# print(f"Число PI: {pi}")
# print(f"Число PI: {round(pi, 2)}")
# print(f"Число PI: {pi:.2f}")

# x = 10
# y = 5
# print(f"{x = }, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")


# a = 74
# print(f"{{{{{a}}}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')

# s = "Много " \
#     "строк"
# s1 = ''
# s3 = """
# Много
#     строк"""
# s4 = '''Много
#     строк'''
# print(s)
# print(s3)
# print(s4)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)


# from geometry import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('м'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me "
# arr = [ord(i) for i in my_str]
# print("ASCII коды:", arr)
#
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
#
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
#
# print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(1080))

# a = 97
# b = 122
# # if a > b:
# #     print([chr(i) for i in range(b, a + 1)])
# # else:
# #     print([chr(i) for i in range(a, b + 1)])
# if b > a:
#     a, b = b, a
# # print([chr(i) for i in range(b, a + 1)])
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# print('apple' == 'Apple')  # 97 == 65
# print('apple' < 'Apple')  # 97 < 65
# print(ord('a'))
# print(ord('A'))


# from random import randint
#
# short = 7
# long = 10
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(min_ASCII, max_ASCII))
#         res += rand_char
#
#     return res
#
#
# print("Случайный пароль:", random_password())


# Методы строк
# print(dir(list), "\n")
# print(dir(str))

# s = "hello, WORLD! I am learning Python."

# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.


# print(s.count("h", 1, -5))  # подсчет количества вхождений подстроки в строку
# print(s.find("h"))  # Возвращает первый индекс, который соответствует началу подстроки или -1 если элемента нет
# print(s.rfind("h"))  # Возвращает последний индекс
#
# print(s.index("h"))  # Возвращает первый индекс, который соответствует началу подстроки или
# # ValueError если элемента нет
# print(s.rindex("h"))  # Возвращает последний индекс


# s = "один два"
# one_word = s[:s.find(' ')]  # [:4]
# print(one_word)
# two_word = s[s.find(' ') + 1:]  # [4 + 1:]
# print(two_word)
# print(two_word + ' ' + one_word)

# s1 = 'ab12c59p7dq'
# digits = []
# # for symbol in s1:
# #     if '1234567890'.find(symbol) != -1:
# #         digits.append(int(symbol))
#
# print(digits)

#
# st = 'The original words and form of a written or printed work'
# ch = "f"
# if st.count(ch) == 1:
#     print(st.find(ch))
# elif st.count(ch) >= 2:
#     print(st.find(ch), st.rfind(ch))


# print(s.endswith('lo', 0, 5))  # строка заканчивается заданными символами
# print(s.startswith('I am', 14))  # строка начинается с заданных символов

# print('Aabc123'.isalnum())  # определяет состоит ли строка из букв и цифр
#
# print('abcABC'.isalpha())  # определяет состоит ли строка из букв
# print('456123'.isdigit())  # определяет состоит ли строка из цифр
#
# print('abc456'.islower())  # определяет состоит ли строка из символов букв в нижнем регистре (могут присутствовать
# # любые символы)
#
# print('ADF456'.isupper())  # определяет состоит ли строка из символов букв в верхнем регистре (могут присутствовать
# любые символы)

# print("py".center(10))  # выравнивает строку по центру
# print("py".center(10, "-"))
# print("py".center(1))

# print('     py'.lstrip())
# print('py     '.rstrip())
# print('    py     '.strip())

# print('https://www.python.org'.lstrip("/:pthsworg"))
# print('https://www.python.org'.rstrip("/:pthsworg"))
# print('https://www.python.org'.strip("/:pthsworg"))
#
#
# print('https://www.python.org'.lstrip("/:pths").rstrip("org."))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python", 2))

# s = "Заменить в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения."
# a = s[:s.find('о') + 1]
# b = s[s.find('о') + 1:s.rfind('о')]
# c = s[s.rfind('о'):]
# s = a + b.replace('о', 'О') + c
# print(s)


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# print("".join(['1', '2']))
#
# print(":".join("Hello"))
#
# print("H:e:l:l:o".split(":"))
#
# print("Строка разделенная пробелами".split())
#
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))


# a = input("-> ").split()
# print(a)

# a = input('Введите ФИО: ').split()
# print(a)
# print(f"{a[0].capitalize()} {a[1][0].upper()}. {a[2][0].upper()}.")


# Регулярные выражения
# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в два счёта."
# reg = "в"
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с шаблоном
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))  # месторасположение совпадения объекта в начале строки
# print(re.split(reg, s, 2))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "В", s, 3))  # поиск и замена

# s = "Я ищу совпадения^ в 2023 году. И я их найду в 2 счёта. [-1863]. Hello"
# reg = "[12][0-9][0-9][0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[0-9\[\].-]"
# reg = r"[^А-я]"
# print(re.findall(reg, s))
# print(ord("Ё"))
# print(ord("А"))
# print(ord("я"))
# print(ord("ё"))
# print(chr(96))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T19:50. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения ^ в 2023 году. И я их найду в 2 счё_та. [-1863]. Hello. 200000000"
# reg = r"0+"
# print(re.findall(reg, s))

# d = "Цифры: -7, +17, -42, 0012, 0.33"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# s = "06-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"#.*", "", s))
#
# # Дата рождения: 06.03.1987
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r"#.*", "", s)))
# print('Дата рождения:', re.sub(r'-', '.', "06-03-1987 "))

# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, s))

# s = "12 сентября 2021 года 4567896744541"
# reg = r"\d{,8}"
# print(re.findall(reg, s))

# s = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall(r'^[A-Za-z_0-9-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Pyt_09-4'))


# print(re.findall(r'\w+', '10 + й'))
# print(re.findall(r'\w+', '10 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '10 + й', flags=re.A))
# print(re.findall(r'\w+', '10 + й', re.A))


# text = "hello world"
# # print(re.findall(r"\w+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё_та."
# reg = r"я"
# # print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))


# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, re.DOTALL))
# # print(re.findall(r'one.\w+', text, re.S))
#
# print(re.findall('one$', text))
# print(re.findall('one$', text, re.MULTILINE))
# print(re.findall('^two', text))
# print(re.findall('^two', text, re.M))

# print(re.findall("""
# [a-z.-]+      # part 1
# @             # @
# [a-z.-]+      # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
#
# s = "Я ищу совпадения^ в 2023 году. И я их найду в 2 счёта. 186389. Hello"
# reg = r"\d{2,}?"
# print(re.findall(reg, s))

# s = "<p>Изображение <img  src='bg.jpg' > - фон страницы <img alt='картинка'></p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
#
# print(re.findall(reg, s))
# print(re.sub(reg, "<img src='1.jpg'>", s))


# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))


# s = "int = 4, float = 4.0, double = 8.0f, int 7"
# # reg = r"int\s*=\s*\d[.\w]*|double\s*=\s*\d[.\w]*"
# reg = r"(?:int|double)\s*=\s*(?:\d[.\w]*)"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# () - сохраняющие скобки
# (?:) - несохраняющие скобки


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(?:\d*)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))


# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё_та."
# reg = r"(\d+)\s(\D+)"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_count(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print("<select name='city'>")
# print(re.sub(r'\s*(\w+)\s*', repl_count, text))
# print("</select>")

# s = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2-\1-\3", s))  # 23.10.2021

# s = "yandex.ru and yandex.com"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))  # 3
# elevator(n1)

# 1
# 2
# 3

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         return lst[0]  # 9
#     else:
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):  #
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  #
#     else:
#         return to_str(n // base, base) + convert[n % base]  #
#
#
# print(to_str(254, 8))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]


# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
#
# print(names[1])
# print(isinstance(names[1], list))
#
# print(names[1][1])
# print(isinstance(names[1][1], list))
#
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# def count_items(item_list):  # ["Bob", ["Chet", "Cat"], "Bard", "Bert"]
#     count = 0   #
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)  # 6
#         else:
#             count += 1   # 10
#     return count
#
#
# print(count_items(names))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# count = 0
# for i in range(len(names)):
#     count += 1
#     for j in range(len(names[i]) - 1):
#         if isinstance(names[i], list):
#             count += 1
#             for k in range(len(names[i][j]) - 1):
#                 if isinstance(names[i][j], list):
#                     count += 1
# print(count)


# def remove(text):  # ""
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # HelloWorld
#
#
# print(remove("  Hello\nWorld "))
# print("  Hello\nWorld ")

# print(bool(""))

# Файлы

# f = open(r'D:\Python215\215\text.txt')
# # f = open('text.txt')
# print(f)
# print(*f)
# print(f.mode)
# print(f.encoding)
# print(f.name)
# f.close()
# print(f.closed)

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open('test.txt')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('test.txt')
# print(f.readlines(36))
# print(f.readlines())
#
# f.close()

# count = 0
# f = open('test.txt')
# for line in f:
#     # print(line)
#     count += 1
# f.close()
# print("count:", count)

# f = open('test.txt')
# print(len(f.readlines()))
# f.close()

#
# f = open("xyz.txt", "w")
# f.write('Hello\nWorld\n')
# f.close()


# f = open("xyz.txt", "a")
# # f.write('New text\n')
# line = ['This is line 1', 'This is line 2']
# f.writelines(line)
# f.close()


# f = open("xyz.txt", "w")
# lst = [str(i ** 5) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# f = open('text2.txt', 'w')
# f.write("Заменить строку в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# f.close()
# print(read_file)
# read_file[1] = 'Замена\n'
# print(read_file)
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()


# f = open('text2.txt', 'w')
# f.write('''Заменить строку в текстовом файле;
# изменить строку в списке;
# записать список в файл''')
# f.close()
#
# n = int(input('введите номер строки удаляемой строки '))
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# if 0 < n <= len(read_file):
#     # read_file[n - 1] = ''
#     del read_file[n - 1]
# else:
#     print("Номер строки введен неверно")
# print(read_file)
# f.close()

# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))  # Hel
# print(f.tell())  # 3  - возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # 1  - перемещает условный курсор в заданную позицию
# print(f.read())  # ello!
# print(f.tell())
# f.close()


# f = open('text1.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# with open('text.txt', 'r+') as f:
#     print(f.write('01234\n56789'))
#
#
# with open('text.txt', 'r+') as f:
#     for line in f:
#         print(line[:3])


# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# print(len(lst))
# print(sum(lst))

# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
#
# print('Done!')


# with open('res.txt', 'r') as f:
#     read_file = f.read().split(" ")
#     print(read_file)
#     len(read_file)
#     print(sum(map(float, read_file)))

# def longest_words(file):
#     with open(file) as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         # print(w)
#         # print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words('test.txt'))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# other_file = 'three.txt'
# with open(read_file, 'r') as fr, open(write_file, 'r') as frr, open(other_file, 'w') as fw:
#     # for line in fr:
#     #     line = line.replace("Строка", "Линия - ")
#     #     fw.write(line)
#
#     a = fr.readlines()
#     b = frr.readlines()
#     # print(a)
#     # print(b)
#     # c = a + b
#     # print(c)
#     # # for line in c:
#     # #     fw.write(line)
#     # fw.writelines(c)
#
#     for i, j in zip(a, b):
#         c = i + j
#         fw.write(c)


# Модули OS и OS.PATH

import os

# import os.path

# print("Текущая директория:", os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # возвращает имена файлов и папок из текущей директории
# print(os.listdir(".."))
# os.mkdir("folder")  # создание папки
# os.makedirs("nested1/nested2/nested3")  # создание папки и всех папок
# os.rmdir("folder")  # удаление пустой директории
# os.remove("xyz.txt")  # удаляет файл
# os.rename('two.txt', 'new.txt')  # переименовывает файл или папка
# os.rename('new.txt', 'directory/two.txt')  # перемещает по заданному путь (все имена в пути должны существовать)
# os.rename('three.txt', 'directory/three.txt')
# os.renames('text2.txt', 'test/text.txt')  # создает промежуточные директории


# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk("nested1"):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")

# print(os.path.split(r"D:\Python215\215\nested1\nested2\nested3\text.txt"))  # разбивает путь на кортеж (head, tail),
# # tail - последний компонент пути, head - остальная часть
#
# print(os.path.dirname(r"D:\Python215\215\nested1\nested2\nested3\text.txt"))   # путь до последнего компонента
# print(os.path.basename(r"D:\Python215\215\nested1\nested2\nested3\text.txt"))  # последний компонент пути

# print(os.path.join('215', r'D:\Python215', 'nested1', 'nested2', 'text.txt'))  # соединяет один или несколько
# компонентов пути с учетом особенностей OS


# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
#
#
# files_width_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_width_text:
#     with open(file, 'w') as f:
#         f.write(f"Некоторый текст для документа: {file}")
#
#
# def print_tree(root, topdown=True):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree("Work", False)
# print_tree("Work")

# print(os.path.exists(r"D:\Python215\215\nested1\nested2\nested3\text.txt"))  # возвращает True, если путь указывает
# на существующий файл, False - на несуществующий файл
# import time
#
# path = r'D:\Python215\215\venv\Scripts\python.exe'
# print(os.path.getsize(path) // 1024, "KB")  # возвращает размер файла в байтах
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу
# print(os.path.getctime(path))  # возвращает время создания файла
#
#
# a_time = os.path.getatime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a_time)))
#
#
# print(os.path.isdir(r'D:\Python215\215\venv\Scripts\python.exe'))  # Возвращает True, если путь является директорией
# print(os.path.isfile(r'D:\Python215\215\venv\Scripts\python.exe'))  # Возвращает True, если путь является файлом

# path = r"nested1\nested2\nested3\text1.txt"
#
# if os.path.exists(path):
#     d, name = os.path.split(path)
#     print(f"{name} ({d}), -last access time", os.path.getatime(path))
# else:
#     print("File is not exist")


# class Point:
#     """Класс для предоставления координат точки на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# # print(type(p1))
# # print(p1.x)
# # print(Point.__doc__)
# print(dir(Point))


# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# Point.x = 100
# p1.x = 30
# p1.y = 60
# p1.z = 80
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(Point.__dict__)


# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)

# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# Point.set_coord(p1, 5, 10)
#
#
# p2 = Point()
# # p2.x = 20
# # p2.y = 40
# p2.set_coord(20, 40)
# # Point.set_coord(p2)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.address = address
#         self.birthday = birthday
#         self.city = city
#         self.phone = phone
#         self.country = country
#         self.name = first_name
#
#     def set_city(self, city):  # установить
#         self.city = city
#
#     def get_city(self):  # получить
#         return self.city
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_city("Саратов")
# print(h1.get_city())
# h1.set_name('Вася')
# print(h1.get_name())
# h1.set_birthday("09.11.2013")
# print(h1.get_birthday())
# h1.set_phone("78-45-92")
# print(h1.get_phone())
# h1.set_country("Беларусь")
# print(h1.get_country())
# h1.set_address("Ленина")
# print(h1.get_address())
# h1.print_info()


# class Person:
#     skill = 10  # статическое свойство
#
#     def __init__(self, name, surname):
#         self.name = name  # динамическое свойство
#         self.surname = surname  # динамическое свойство
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# # del p1
# p1 = 0
# print(p1.x)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if isinstance(x, int) and isinstance(y, int):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(20, 30)
# print(p1.get_coord())


# class Point:
#     count = 0  # 3
#
#     def __init__(self, x=1, y=1):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print("Point", Point.count)
# print("p1", p1.count)
# print("p2", p2.count)
# print("p3", p3.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним.")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# print()
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# print()
# droid3 = Robot('RT-H2')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("Роботы закончили свою работу. Давайте их выключим.\n")
#
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должна быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10.2)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = "aaaa"
# print(p1.__dict__)
# print(p1.get_coord())
# p1.set_coord(80.2, 120)
# print(p1.get_coord())
# p1.set_x(4)
# print(p1.get_x())
# p1.set_y(24)
# print(p1.get_y())
# print(p1.get_coord())
# import geometry
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_width(self, w):
#         if Rectangle.__check_value(w):
#             self.__width = w
#
#     def set_length(self, lg):
#         if Rectangle.__check_value(lg):
#             self.__length = lg
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__width * self.__length
#
#     def get_perimetr(self):
#         return 2 * (self.__width + self.__length)
#
#     def get_hypotenuse(self):
#         return round(geometry.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(('*' * self.__width + "\n") * self.__length)
#
#
# a = Rectangle()
# a.set_length(3)
# a.set_width(9)
# print("Длина прямоугольника:", a.get_length())
# print("Ширина прямоугольника:", a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimetr())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.get_draw()


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_x(self, x):
#         if Point.__check_value(x):
#             print("__set_x")
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # p1.__set_x(45)
# p1.x = 45
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         print("__get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             print("__set_x")
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # p1.__set_x(45)
# p1.x = 45
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             raise TypeError("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")
# weight.kg = '10.5'
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Irina', 26)
# print(p1.__dict__)
# p1.name = 'Ira'
# print(p1.name)
# p1.old = 22
# print(p1.old)
# del p1.old
# print(p1.__dict__)


# class Point:
#     __count = 0  # 1 2 3
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(p1.get_count())
# print(p2.get_count())
# print(p3.get_count())
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# import geometry
#
#
# class Area:
#     __count = 0
#
#     @staticmethod
#     def triangle_area_1(a, b, c):
#         Area.__count += 1
#         p = (a + b + c) / 2
#         return geometry.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area_2(a, h):
#         Area.__count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.__count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.__count
#
#
# print(f"Площадь треугольника по формуле Герона (3,4,5): {Area.triangle_area_1(3, 4, 5)}")
# print(f"Площадь треугольника через основание и высоту (6,7): {Area.triangle_area_2(6, 7)}")
# print(f"Площадь квадрата (7): {Area.square_area(7)}")
# print(f"Площадь прямоугольника (2,6): {Area.rect_area(2, 6)}")
# print(f"Количество подсчетов площади: {Area.get_count()}")

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split('.'))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(string_date):
#         if string_date.count('.') == 2:
#             day, month, year = map(int, string_date.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '01.01.2021',
#     '12.31.2020'
# ]
#
# for sting_date in dates:
#     if Date.is_date_valid(sting_date):
#         date = Date.from_string(sting_date)
#         print(date.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")


# string_date = '23.10.2022'
# day, month, year = map(int, string_date.split('.'))

# date = Date(day, month, year)
# date = Date.from_string('23.10.2022')   # date = Date(day, month, year)
# print(date.string_to_db())
# date2 = Date.from_string('21.12.2023')
# print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_usd_rate(2)
# acc.set_eur_rate(3)
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
#
# print()
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def virify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.virify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.5)
# p1.fio = "Соболев Игорь Николаевич"
# print(p1.fio)
# p1.old = 42
# print(p1.old)
# p1.password = '4567 123456'
# print(p1.password)
# p1.weight = 70.5
# print(p1.weight)
# print(p1.__dict__)

# print(issubclass(Point, object))


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределение инициализатора для класса Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20), 'green', 5)
# # print(line.__width)
# line.draw_line()

# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# DRY (Don`t Repeat Yourself) - не повторяйся


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.__width = width
#         self.__height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина прямоугольника должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота прямоугольника должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника {self.__width}x{self.__height}:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect.color)
# print(rect.area())
# print(rect.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(5.5, 14.2), Point(30.2, 54.6))
# line.draw_line()
# print()
# rect = Rect(Point(10, 20), Point(200, 300))
# rect.draw_rect()
# rect.set_coord(Point(5, 14), Point(30, 54.0))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Фон: {self.fon}")
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.bord = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.bord}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))  # " ".join([1, 2, 3])
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))
#
# print(" ".join(['1', '2', '3']))


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Первая координата должны быть целыми числом")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# rect = Rect(Point(1, 2), Point(10, 20))
# rect.draw_rect()
# rect.set_coord(Point(10, 30), Point(40, 70))
# rect.draw_rect()
# rect.set_coord(Point(-10, -20))
# rect.draw_rect()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     # def draw(self):
#     #     print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     ...
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # Абстрактный метод
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()

# from geometry import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t3 = SqTable(20)
# print(t3.__dict__)
# print(t3.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# elem = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
#
# for d in elem:
#     d.print_value()
#     print(f"= {d.convert_to_rub():.2f} RUB")
#
#
# print()
# elem2 = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for s in elem2:
#     s.print_value()
#     print(f" = {s.convert_to_rub():.2f} RUB")


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# def func():
#     x = 2
#
#     def inner():
#         n = 4
#         return n + x
#
#     return inner
#
#
# a = func()
# b = a()
# print(b)


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("outer_class_method")
#
#     def outer_obj_method(self):
#         print('outer_obj_method')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("inner_method", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#         self.imp = Employee().Head()
#
#     def display(self):
#         print('Name:', self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         # self.intern = Intern()
#         # self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)  #, self.intern.name
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#
#         def display(self):
#             print('Name:', self.name)
#
#
# intern = Intern()
# a = intern.imp
# print(a.name)

# outer = Employee()
# outer.show()
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Внешний класс")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Вложенный класс")
#
#         class InnerClass:
#             def show(self):
#                 print('Класс внутри вложенного класса')
#
#
# outer = Outer()
# outer.show()
#
# # inner1 = outer.inner
# # inner1.show()
#
# # inner2 = inner1.inner_inner
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Widows 10"
#
#     class CPU:
#         def make(self):
#             return "intel"
#
#         def model(self):
#             return 'Core-i7'
#
#
# # comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# # print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     # def __init__(self):
#         # self.db = self.Inner()
#
#     def display(self):
#         print("Базовый класс")
#
#     class Inner:
#         def display1(self):
#             print("Вложенный класс внутри базового")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("Дочерний класс")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Вложенный класс внутри дочернего')
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок"), Cat('Мурзик')]
# print(cat)

# class Point:
#     def __init__(self, *args):
#         print(args)
#         self.__coord = args
#         self.length = 0
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 9, 4)
# print(len(p))
# import geometry
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(5, 10)
# print(p1.length)
# p1.length = 10
# print(p1.length)
# print(p1.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p2 = Point2D(5, 10)
# print('p1 =', p1.__sizeof__())
# print('p2 =', p2.__sizeof__() + p2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         self.z = z
#         super().__init__(x, y)
#
#
# p1 = Point(5, 10)
# p3 = Point3D(5, 10, 20)
# # p3.z = 20
# print(p3.x, p3.y, p3.z)


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, "is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name, "is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name, "is barking")
#
#
# b = Dog("Buddy")
# b.bark()
# b.sleep()
# b.play()

# class A:
#     def __init__(self):
#         print("Класс A")
#
#
# class AA:
#     def __init__(self):
#         print("Класс AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Класс B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Класс C")
#
#
# class D(B, C):
#     # def __init__(self):
#     #     print("Класс D")
#     pass
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)

# class A:
#     def __init__(self):
#         print('Class A')
#
#     def hi(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print('Class B')
#
#     def hi(self):
#         print("B")
#
#
# class C(A):
#     def __init__(self):
#         print('Class C')
#
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     def __init__(self):
#         print('Class D')
#         B.__init__(self)
#         C.__init__(self)
#
#     def hi(self):
#         print("D")
#         A.hi(self)
#
#
# d = D()
# d.hi()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор POS")
#         self._sp = sp
#         self._ep = ep
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     # def __init__(self, sp, ep, color="red", width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Styles.__init__(self, color, width)
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)  #
# l1.draw()


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a', encoding='utf-8') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет отображаться и записываться в файл")

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def price_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_save_log(self):
#         print(f"{self.id}: товар был продан в 00:00")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n1 = NoteBook('HP', 1.5, 35000)
# n.price_info()
# n.save_save_log()
# n1.save_save_log()
# print(NoteBook.mro())


# 24 * 60 * 60 = 86400 (число секунд в одном дне)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)  # Clock(300)
#
#     def __eq__(self, other):
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# c2 += c1
# print(c2.get_format_time())
# print(type(c3))
# print(c3.get_format_time())

# print(5 == 2)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # off = 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value  # # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#
#         del self.marks[key]
#
#
# s1 = Student("Виктор", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# print([None] * 6)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)  # Clock(300)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         elif item == 'min':
#             return (self.sec // 60) % 60
#         elif item == 'sec':
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])
# c1['hour'] = 9
# c1['min'] = 3
# c1['sec'] = 68
# print(c1['hour'], c1['min'], c1['sec'])
# print(c1.get_format_time())

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]  # range(0, 1)
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# # cat3 = Cat("Murzik", 5, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)

# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# for g in shape:
#     if isinstance(g, Rectangle):
#         print(g.get_per_rect())
#     else:
#         print(g.get_per_sq())

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)  # 10 + 35
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))  # len('10' + str(35)) => len('1035') => 4
#
#
# t1 = Number(10)
# t2 = Text('10')
#
# print(t1.total(35))
# print(t2.total(35))
#
# print(5 + 2)  # 7
# print('5' + '2')  # 52


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         return f'{self.name} мяукает'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         return f'{self.name} гавкает'
#
#
# shape = [Cat("Пушок", 2.5), Dog("Мухтар", 4)]
# for a in shape:
#     a.info()
#     print(a.make_sound())

# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         super().__init__(surname, name, age)
#         self.rating = rating
#         self.group = group
#         self.speciality = speciality
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, experience):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#         super().__init__(surname, name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# Функторы

# def func():
#     def wrap():
#         return "Hello"
#
#     return wrap
#
#
# a = func()
# print(a())

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(self.count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c1()

# class StripChars:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         # print(string)  # ' !  ?Hello World; . :'
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(self.chars)
#
#
# s1 = StripChars("?;!.: ")
# print(s1(" !  ?Hello World; . :"))
#
#
# # print(s1(20))
#
# def strip_char(chars):
#     def call(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return call
#
#
# s2 = strip_char("?;!.: ")
# print(s2(" !  ?Hello World; . :"))


# Декораторы

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def hello():
#     print("Hello")
#
#
# hello()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(a, b))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def result(a, b):
#     return a * b
#
#
# print(result(2, 3))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(*args, **kwargs))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# @MyDecorator
# def hello1(a, b, c):
#     return a * b * c
#
#
# print(hello(2, 5))
# print(hello1(2, 5, 2))
# print(hello1(a=2, c=5, b=2))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = 'перед вызовом функции\n'
#             res += self.arg + str(func(*args, **kwargs))
#             res += '\nпосле вызова функции'
#             return res
#
#         return wrap
#
#
# @MyDecorator("Результат умножения: ")
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return func(*args, **kwargs) ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def result(a, b):
#     return a * b
#
#
# print(result(2, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person('Виталий', 'Карасев')
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def method_2(self, value):
#             # print("cls =", cls)
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def method_1(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method_1(4))
# print(obj.method_2(4))


# Дескрипторы
#
# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# p.name.set("Виктор")
# print(p.name.get())

# class ValidSting:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     first = ValidSting()
#     surname = ValidSting()
#
#     def __init__(self, name, surname):
#         self.first = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# p.first = "Владимир"
# print(p.first)
# print(p.surname)
# print(p.__dict__)

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.z = 15
# print(p1.z)
# print(p1.__dict__)


# Создание модулей

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
#
#
# import math

# import start

# start.run()

# from car.electrocar import ElectroCar
#
#
# def main():
#     car = ElectroCar('Tesla', 'T', 2018, 99000)
#     car.show_car()
#     car.description_battery()
#
#
# if __name__ == '__main__':
#     main()


# Упаковка данных (сериализация)
# Распаковка данных (десериализация)

# marshal (*.pyc)
# pickle
# json

# dump() - сохраняет данные в открытый файл
# load() - считывает данные из открытого файла

# dumps() - сохранять данные в строку
# loads() - считывает данные из строки

# import pickle


# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': 'морковь',
#     'бюджет': 1000
# }
#
# # with open(file_name, 'wb') as f:
# #     pickle.dump(shop_list, f)
#
# with open(file_name, 'rb') as f:
#     shop_list_2 = pickle.load(f)
# print(shop_list_2)

# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#     d = {'first': 'a', 'second': 2}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}\nСловарь: {Test.d}"
#
#
# obj = Test()
# # print(obj)
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
# obj = pickle.loads(my_obj)
# print(obj)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# import json

# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstname': 'Alice',
#             'age': 6
#         }
#     ]
# }

# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4)
#
# with open('data_file.json') as f:
#     data1 = json.load(f)
# print(data1)

# json_string = json.dumps(data, sort_keys=True)
# # print(json_string)
# # print(type(json_string))
# # print(json_string[:20])
#
# data1 = json.loads(json_string)
# print(data1)
# print(type(data1))
# print(data1['name'])

# x = {
#     "name": "Виктор"
# }
# d = json.dumps(x)
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
# data1 = json.loads(d)
# print(data1)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'm', 'n', 'k']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):  # {'name': 'dfsdfdsf', 'tel': '7894452154'}
#     try:
#         data = json.load(open('persons.json'))  # [{'name': 'dsdfdsf', 'tel': '4523452154'}]
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)  # [{'name': 'dsdfdsf', 'tel': '4523452154'}, {'name': 'dfsdfdsf', 'tel': '7894452154'}]
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)  # [{'name': 'dsdfdsf', 'tel': '4523452154'}, {'name': 'dfsdfdsf', 'tel': '7894452154'}]
#
#
# for i in range(5):
#     write_json(gen_person())


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'm', 'n', 'k']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):  # {'name': 'dfsdfdsf', 'tel': '7894452154'}, '7894452154'
#     try:
#         data = json.load(open('persons1.json'))  # {'dfsdfdsf': {'name': 'dfsdfdsf', 'tel': '7894452154'}}
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict  # {'7894452154': {'name': 'dfsdfdsf', 'tel': '7894452154'},
#     # '4584452154': {'name': 'dfsdfdsf', 'tel': '7894452154'}}
#     with open('persons1.json', 'w') as f:
#         json.dump(data, f, indent=2)  # {'dfsdfdsf': {'name': 'dfsdfdsf', 'tel': '7894452154'}}
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# [{}, {}, {}]

# {
#     'a': {},
#     'b': {},
#     'c': {}
# }

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += str(i) + ", "
#         # return f"Студент: {self.name} - {a[:-2]}"
#         a = ", ".join(map(str, self.marks))
#         return f"Студент: {self.name} - {a}"
#
#     # def __repr__(self):
#     #     a = ", ".join(map(str, self.marks))
#     #     return f"Студент: {self.name} - {a}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': self.name, 'marks': self.marks})
#         with open(file_name, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])  #
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_journal(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# # file1 = 'Student_list.json'
# # st1.dump_to_json(file1)
# # st1.load_from_file(file1)
# # st3.dump_to_json(file1)
# # Student.load_from_file(file1)
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(1, 5)
# # print(st1)
# # print(st1.average_mark())
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# # # print(my_group)
# my_group.add_student(st3)
# # # print()
# # # print(my_group)
# my_group.remove_student(1)
# # # print()
# # print(my_group)
# # print()
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# # print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# # print()
# # print(my_group)
# # print()
# # print(my_group2)
# file2 = 'group_list.json'
# my_group2.dump_group(file2)
# Group.upload_journal(file2)


# pip install requests

# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# # print(type(response.text))
# todos = json.loads(response.text)
# # print(type(todos))
# # print(todos)
#
# # {1: 3, 2: 3}
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# # top_users = sorted(todos_by_user.values(), reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
#
# max_user = " and ".join(users)
# print(max_user)
#
# n = 's' if len(users) > 1 else ''
# print(f"User{n} {max_user} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count  # False and True
#
#
# with open('filtered_data.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#
#     json.dump(filtered_todos, f, indent=2)


# CSV (Comma Separated Values - переменные, разделенные запятыми)

# import csv

# with open('data.csv') as f:
#     file_reader = csv.reader(f, delimiter=";")  # []
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")

# with open('data2.csv') as f:
#     file_reader = csv.reader(f, delimiter=';')
#     for row in file_reader:
#         print(row)


# with open('data.csv') as f:
#     fields = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=fields)  # {}
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)


# with open('student1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Вова", "Возраст": "14"})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]

# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# with open('todos.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)
#
# print(list(todos[0].keys()))


# import requests

# pip install beautifulsoup4 или bs4

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find("div", class_="name").text
# # row = soup.find_all("div", class_="name")
# # row = soup.find_all("div", class_="row")[1].find('div', {"data-set": "salary"})
# # row = soup.find("div", string="Alena").parent
# # row = soup.find("div", string="Alena").find_parent("div", class_="row")
# # row = soup.find("div", id="whois3").find_next_sibling()
# # row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", class_="row")
# copywriter = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)


# import requests

# res = requests.get("https://ru.wordpress.org/")
# res.encoding = 'utf-8'
# # print(res.headers['content-type'])
# # print(res.content)
# print(res.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find('header', id="masthead").find('p', class_='site-title').text
#     print(p1)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r'\D+', '', s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[3]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get('href')   # ["href"]
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins_1.csv", 'a') as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find('h3').find("a")["href"]
#         except ValueError:
#             url = ""
#
#         try:
#             snippet = el.find('div', class_="entry-excerpt").find('p').text
#         except ValueError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 5):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# articles = {"w": 5, "t": 4}
#
# for ind, article in enumerate(articles, 5):
#     print(f"{ind}. {article}")

import socket

URLS = {
    '/': "index page",
    '/blog': 'blog page'
}


def parse_request(request):
    parsed = request.split()
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method, url):
    if method != 'GET':
        return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Page Not Found\n\n', 404
    return 'HTTP/1.1 200!\n\n', 200


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = URLS[url]
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(f"Клиент: {addr} => \n{request}\n")

        response = generate_response(request.decode())
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
