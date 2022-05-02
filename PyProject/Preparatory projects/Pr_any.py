# friend = ('Я даже не знаю, что здесь и написать')
# friend.split()
# print(friend.split())
# -------------------------------------------------------
# name = 'Leo'
# age = 30
# man = 'ужтк'
#
# hello = 'Привет, ' + name +  ' тебе ' + str(age) + ' лет '
# print(hello)
#
# hello = 'Привет, %s тебе %d лет'%(name, age)
# print(hello)
#
# hello = 'Привет, {} тебе {} лет'.format(name,age)
# print(hello)
# ---------------------------------------------------------------------------------------------
# top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
#
# start = top5.find('1')
# end = top5.find('4')
#
# top3 = top5[start:end]
#
# result = 'Поздравляем {} с успехом!'.format(top3.upper())
# print(result)
# ---------------------------------------------------------------------------------------------
# hero = 'Superman'
#
# if hero.find('an') != -1:
#     print('Yes!')
#     print(hero.find("an"))
#
# if 'an' in hero:
#     print('Yes!')
# ---------------------------------------------------------------------------------------------
# top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
# list = top5.split()
# print(list)
# if 'соревнованиях:' in list:
#     print('Yes!')
# else:
#     print('Ooops!')
# ---------------------------------------------------------------------------------------------
# friend_name = 'Max'
# friends = ['Max', 'Leo', 'April', 'Zed']
# roles = ('admin', 'user', 'guest')
#
# # while
# i = 0
# while i < len(friends):
#     friend = friends[i]
#     print(friend)
#     i+=1
#
# # for
# for friend in friends:
#     print(friend)
#
# for role in roles:
#     print(role)
#
# for letter in friend_name:
#     print(letter)
# ---------------------------------------------------------------------------------------------
# friend = {
#     'name': 'Jack',
#     'age': 42,
#     'surname': 'Sperrow',
#     'number': '8945'
# }
#
# friend['has_car'] = 'Конечно, он же богатый урод!'
#
# friend['has_car'] = True
#
# del friend['has_car']
#
# user = input('Chto ti hochesh yznat pro moego dryga?')
# print(friend[user])
# ---------------------------------------------------------------------------------------------
# friend = {
#     'name': 'Jack',
#     'age': 42,
#     'surname': 'Sperrow',
#     'number': '8(999)543-26-91'
# }
# # по ключам
# for key in friend.keys():
#     print(key)
#     print(friend[key])
#
# for key in friend:
#     print(key)
#     print(friend[key])
#
# # по значениям
# for val in friend.values():
#     print(val)
#
# # по парам ключ значение
# for item in friend.items():
#     print(item)
#
# for key, val in friend.items():
#     print(key)
#     print(val)
# ---------------------------------------------------------------------------------------------
# cities = ['Moscow', 'Paris', 'London', 'Paris', 'Tula', 'Paris', 'Moscow']
# cities = set(cities)
# print(cities)
# cities = {'paris', 'moscow', 'paris', 'moscow', 'paris', 'moscow', 'paris', 'moscow', 'paris', 'moscow'}
# print(cities)
# ---------------------------------------------------------------------------------------------
# cities = {'Paris', 'Moscow', 'London', 'Tula'}
#
# cities.add('Burma')
# print(cities)
#
# cities.remove('Burma')
# print(cities)
#
# user_ans = input('Введите название города, который может быть в этом списке\n')
# user_ans= user_ans.lower()
#
# cities = str(cities)
# cities = cities.lower()
#
# if user_ans in cities:
#     print('Тут реально есть такой городишка!)')
# else:
#     print('Ну, не знаю, пока что ничего подобного(')
# ---------------------------------------------------------------------------------------------
# max_things = {'Шорты', ' Бритва', 'Телефон', 'Рубашка'}
#
# kate_things = {'Шорты', 'Телефон', 'Помада', 'Зонт'}
#
# print(max_things | kate_things)
#
# print(max_things & kate_things)
#
# print(max_things - kate_things)
#
# print(kate_things - max_things)
# ---------------------------------------------------------------------------------------------
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
#
# for number in my_list_1[:]:
#     if number in my_list_2:
#         my_list_1.remove(number)
# print(my_list_1)
# ---------------------------------------------------------------------------------------------
# import random
# number = random.randint(1, 100)
#
# change = input('Здравтвуйте, компьютер загадал число от 1 до 100. Мы предлагаем вам отгадать это число. Вы с нами?\nВаш ответ: ')
# user_ans = None
# levels = {1: 10, 2: 5, 3: 3}
# count = 0
#
# if change == 'да':
#     players = int(input('Введите количество игроков от 1 до 3: '))
#     players_count = []
#     if players > 3:
#         print('ВЫ ИДИОТ!!!\nИгра окончена!')
#         exit()
#     else:
#         for i in range(players):
#             player_name = input(f'Введите имя пользователя №{i+1}: ')
#             players_count.append(player_name)
#             for af in players_count:
#                 print(af)
#
#     change_lvl = int(input('Выберите уровень сложности от 1 до 3, где 1 - самый простой, а 3 - самый сложный: '))
#     if change_lvl > 3:
#         print('ВЫ ИДИОТ!!!\nИгра окончена!')
#         exit()
#     max_count = levels[change_lvl]
#     print('Прекрасно! Начинаем!)')
#
#     while (user_ans != number):
#         count += 1
#         if max_count < count:
#             print('Извините, но у вас закончились попытки.')
#             break
#         for player in players_count:
#             user_ans = int(input(f"Попытка №{count}\n{player}, введите число: "))
#             if user_ans == number:
#                 print(f'{player}, поздравляем!!! Вы абсолютно верно ввели загаданное число!)')
#                 break
#             if user_ans < number:
#                 print('Ваше число меньше задуманного числа, попробуйте еще раз, пожалуйста.')
#             else:
#                 print('Ваше число больше задуманного числа, попробуйте еще раз, пожалуйста.')
#
# else:
#     print('Эхх, ну что ж, очень жаль. Всего хорошего.')
#
# print('Спасибо, что играли с нами, ждем вас снова!!!')
# ---------------------------------------------------------------------------------------------
# import random
#
# print('Добро пожаловать в игру, где компьютер постарается угадать, число, которое придумаете вы сами.\nЗдесь есть лишь '
#       'одно условие загаданное число должно находится в промежутке от 0 до 100.')
# min_number = 1
# max_number = 100
# number_comp = random.randint(min_number, max_number)
# user_answer = None
#
# while user_answer != '=':
#     print(number_comp)
#     user_answer = input('Если число верно нажмите "=", если неверно, выберите знак, когда загаданное число больше - ">", '
#                     'когда загаданное число меньше - "<"\nВаш ответ: ')
#     if user_answer == '<':
#         max_number = number_comp - 1
#         number_comp = random.randint(min_number, max_number)
#     else:
#         min_number = number_comp + 1
#         number_comp = random.randint(min_number, max_number)
# print("Приносим свои искрение извинения, но компьютер победил. Спасибо за игру. "
#           "До скорой встречи!")
# ---------------------------------------------------------------------------------------------
# user_answer = input('Введите три любых числа: ')
# numbers_list = []
# for i in user_answer:
#     numbers_list.append(int(i))
#
# print(numbers_list)
#
# print(min(numbers_list))
# print(max(numbers_list))
#
# list = []
# list.append(min(numbers_list))
# list.append(max(numbers_list))
# print(sum(list))
# ---------------------------------------------------------------------------------------------
# def print_sep(sep, len_sep):
#     print(sep * len_sep)
# print_sep('7', 150)
#
#
#
# def get_sep(sep, sep_len):
#     return sep * sep_len
# user = get_sep('7', 50)
# text = f'hello, {user}, func {user}'
# print(text)
# ---------------------------------------------------------------------------------------------
# def hello(who, how_many, where):
#     print(who, how_many,'год(а), проживает в городе',where)
#
# name = input('Введите имя пользователя: ')
# years = int(input('Введите возраст пользователя: '))
# city = input('Введите название города: ')
#
# hello(name, years, city)
# ---------------------------------------------------------------------------------------------
# def greeting(say, *args):
#     print(say, args)
# greeting('hello', 'Leo', 'max', 'alex')
#
# def get_person(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
# get_person(name = 'Leo', age = 20, has_car = True)
# ---------------------------------------------------------------------------------------------
# m = 'Привет, я - глобалочка!'
#
# def a():
#     print(m)
#     ma = 'Меня видно в a(), b() и в c()'
#     print(ma)
#
#     def b():
#         print(m)
#         print(ma)
#         mb = 'Меня видно в b() и в c()'
#
#         def c():
#             print(m)
#             print(ma)
#             print(mb)
#             mc = 'Меня видно в c()'
#             print(mc)
#         c()
#     b()
# a()
# # ---------------------------------------------------------------------------------------------
# def my_filter(numbers):
#     results = []
#     for number in numbers:
#         if number % 2 == 0:
#             results .append(number)
#         return results
# numbers = [1,2,3,4,5,6,7,8,9]
# print(my_filter(numbers))
# ---------------------------------------------------------------------------------------------
# Дебильный калькулятор v1:
#
# what = input("Что же мы делаем? (+, -) ")
#
# a = int(input("Введи первое число "))
# b = int(input("Введи второе число "))
#
#
#
# if what == "+":
#     c = a + b
#     print("Результат: " + str(c))
# elif what == " -":
#     c = a - b
#     print("Результат: " + str(c))
# else:
#     print("Выбрана неверная операция!")
# ---------------------------------------------------------------------------------------------
# Дебильный калькулятор v2:
# from colorama import init
# from colorama import Fore, Back, Style
# init()
#
# print(Fore.LIGHTCYAN_EX)
#
# what = input("Что же мы делаем? (+, -) ")
#
# a = int(input("Введи первое число "))
# b = int(input("Введи второе число "))
#
#
#
# if what == "+":
#     c = a + b
#     print("Результат: " + str(c))
# elif what == "-":
#     c = a - b
#     print("Результат: " + str(c))
# else:
#     print("Выбрана неверная операция!")
# ---------------------------------------------------------------------------------------------
# Программа предоставления услуг погоды!
# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps
# from pyowm.utils.config import get_default_config
# config_dict = get_default_config()
# config_dict['language'] = 'ru'
#
# owm = OWM('f109841ff83b3c23e3f360d219a05ef5')
# mgr = owm.weather_manager()
#
# place = input("В каком городе/стране?: ")
#
# observation = mgr.weather_at_place(place)
# w = observation.weather
#
# temp = w.temperature("celsius")["temp"]
#
# print("Сейчас в " + place + " " + w.detailed_status)
# print("Температура сейчас в районе: " +str(temp))
#
# if temp < 10:
#     print("Сейчас ппц как холодно! Но погулять, в принципе, можно.")
# else:
#     print("Температура норм.")
# ---------------------------------------------------------------------------------------------
# import telebot
# from pyowm import OWM
# from pyowm.utils.config import get_default_config
# config_dict = get_default_config()
# config_dict['language'] = 'ru'
#
# owm = OWM('f109841ff83b3c23e3f360d219a05ef5')
# mgr = owm.weather_manager()
#
# bot = telebot.TeleBot("5055640522:AAHRIo1rAVOPvBNX5uhzCJk8aNHK6MogZNY")
#
# @bot.message_handler(content_types=['text'])
# def send_echo(message):
#     observation = mgr.weather_at_place(message.text)
#     w = observation.weather
#
#     temp = w.temperature("celsius")["temp"]
#
#     answer = "Сейчас в " + message.text + " " + w.detailed_status + "\n"
#     answer += "Температура сейчас в районе: " +str(temp) + "\n\n"
#
#     if temp < 10:
#         answer += "Сейчас ппц как холодно! Но погулять, в принципе, можно. Особенно, если вы сейчас с малышиком в животике)))"
#     else:
#         answer += "Температура норм."
#
#     bot.send_message(message.chat.id, answer)
#
# bot.polling( none_stop = True)
# ---------------------------------------------------------------------------------------------
#  Написать функцию num translate(), переводящую числитеные от 0 до 10 с английского на русский язык.
#
# def num_translae():
#     number = input('Введите число на англ.: ')
#     print(numbers.get(number))
#
# numbers = {
#     'one': 'один',
#     'two': 'два',
#     'three': 'три',
#     'four': 'четыре',
#     'five': 'пять',
#     'six': 'шесть',
#     'seven': 'семь',
#     'eight': 'восемь',
#     'nine': 'девять',
#     'ten': 'десять'
# }
#
#
# num_translae()
# # ---------------------------------------------------------------------------------------------
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(numbers)
#     return result
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# def big_4(number):
#     return number > 4
#
# print(my_filter(numbers, big_4))
# ---------------------------------------------------------------------------------------------
# winter_months = ['декабрь', 'январь','февраль']
# print(type(winter_months) == list)
# print(isinstance(winter_months, list))
#
# print(dir(winter_months))
#
# cur_winter_months = winter_months.pop()
# print(winter_months)
# print(cur_winter_months)
#
# # basket_prices = [3000.0, 1580.0, 3000.0, 2785.0]
# # print(basket_prices.count(3000.0))
# # print(basket_prices.index(3000.0))
# # print(basket_prices.index(4000))
#
# print(winter_months)
#
# winter_months.insert(1, 'январь')
# print(winter_months)
#
# winter_months.extend(['январь', 'январь', 'январь', 'январь'])
# while winter_months.count('январь') > 1:
#     winter_months.remove('январь')
#     print(winter_months)
#
# winter_months = ['декабрь', 'январь','февраль']
# print(id(winter_months), winter_months)
# winter_months.reverse()
# print(id(winter_months), winter_months)
#
# revers_winter_months = list(reversed(winter_months))
# print(revers_winter_months)