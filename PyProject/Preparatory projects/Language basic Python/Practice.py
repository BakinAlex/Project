# Отработка использования функций print() input() и изменение type функции input()
# с помощью int() перед функцией input()
#
# age = int(input('Сколько вам лет?: '))
# period = 20
# age_period = age + period
# print('Через', period, 'вам будет', age_period)


# Игра угадай число
#
# number = 49
# user_number = int(input('Добро пожаловать в игру "Угадай число!" \nВведите число: '))
# if user_number == number:
#     print('Поздравляем, вы угадали число!!!')
# else:
#     if user_number < number:
#         print('Ваше число меньше задуманного')
#     else:
#         print('Ваше число больше задуманного')


# Вывод чисел от 0 до 100:
#
# number = 0
# while number <= 100:
#     print(number)
#     number += 1


# Вывод чисел от 0 до n:
#
# numbers = 0
# user_number = int(input('Введите число: '))
# while numbers <= user_number:
#     print(numbers)
#     numbers += 1


# Вывод четных чисел от 0 до n:
#
# numbers = 0
# user_number = int(input('Введите число: '))
# while numbers <= user_number:
#     if numbers % 2 == 0:
#         print(numbers)
#     numbers += 1


# # ДЗ №1:1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
#   Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
#
# user_number = int(input('Введите число: '))
# print('Сумма равна:', user_number + 2)


# # ДЗ №1: 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
#   После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
#
# while True:
#     user_number = int(input('Введите число от 0 до 10: '))
#     if user_number > 10:
#         print('Вы ввели неправильное число!')
#         continue
#     else:
#         print('Наконец-то. Получается число: ', user_number**2)
#         break


# # ДЗ №1: 3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя
#   следующие данные: имя, фамилия, возраст и вес.
#   Выведите результат согласно которому:
#   Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#   Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
#   Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
#   Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
#
# name = input('Как Вас зовут?: ')
# surname = input('Какая у Вас фамилия?: ')
# age = int(input('Сколько вам лет?: '))
# weight = int(input('Какой у Вас вес?: '))
#
# if age < 30 and  50 <= weight <= 120:
#     print(name, surname, age, 'лет', 'вес', weight, '- вы в хорошем состоянии! Поздравляем!')
# elif age <= 40 and (50 > weight or weight > 120):
#     print(name, surname, age, 'лет', 'вес', weight, '- вам требуется занятся собой)')
# elif age > 40 and (50 > weight or weight > 120):
#     print(name, surname, age, 'лет', 'вес', weight, '- вам требуется медицинский осмотр!!!')
# else:
#     print(name, surname, age, 'лет', 'вес', weight, '- у вас оптимальное состояние.')


# # Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов
# top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
# start = top5.find('1')
# end = top5.find('4')
# top3 = top5[start : end]
# result = 'Поздравляем {} с успехом!!!'.format(top3.upper())
# print(result)


# print('Соревнования по PYTHON')
# amount = int(input('Введите кол-во участников: '))
# members = []
# while amount > 0:
#     name = input('Введите имя {} участника: '.format(amount))
#     members.append(name)
#     amount -= 1
# print('Приветствуем участников {}!!!'.format(members))
# members.reverse()
# result = members[:3]
# print('Поздравляем участников:\n 1 место - {}\n 2 место - {}\n 3 место - {} '.format(result[0], result[1], result[2]))


# # ДЗ №2: 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#
# list_1 = [2, 4, 6, 2, 7, 1, 9, 4, 6, 2, 7, 4]
# list_2 = [4, 7, 2, 9]
# list_3 = list(set(list_1)-set(list_2))
# print(list_3)


# # ДЗ №2: 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде,
#   например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
#
# day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое'}
# month = {'01': 'Января', '02': 'Февраля', '03': 'Марта'}
# user = input('Введите число. Например: "06.03.2013": ')
# dd = user[:2]
# mm = user[3:5]
# yy = user[6:]
# print(day[dd], month[mm].lower(), yy, 'года.')


# # ДЗ №2: 3: Дан список заполненный произвольными целыми числами.
#   Получите новый список, элементами которого будут только уникальные элементы исходного.
#
# list_1 = [2, 2, 5, 12, 8, 2, 12]
# list_2=[]
# for repeat in list_1:
#     if list_1.count(repeat) == 1:
#         list_2.append(repeat)
# print(list_2)


