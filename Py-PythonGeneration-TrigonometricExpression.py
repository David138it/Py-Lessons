'''
Напишите программу, вычисляющую значение тригонометрического выражения
    sin(x)+cos(x)+tan^(2)(x)
по заданному числу градусов x.
'''
from math import *
x = radians(float(input()))
print(sin(x) + cos(x) + tan(x)**2)