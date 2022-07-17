from random import *
num = randint(1,100)
print('Добро пожаловать в числовую угадайку')
'''
Напишите функцию is_valid() в которую передается один строковый аргумент. Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100 и False в противном случае. 
'''
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False
num = input()
print(is_valid(num))
