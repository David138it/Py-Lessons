'''
Профессор Тимур преподает вводный курс статистики и попросил вас написать программу, которую он мог бы использовать на занятиях для имитации бросания игральных кубиков. Программа должна случайным образом генерировать два числа в диапазоне от 11 до 66 и показывать их.
'''
import random
print('Бросаем кубики... ')
print('Значения граней:')
print(random.randint(1, 6))
print(random.randint(1, 6))
