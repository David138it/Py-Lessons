'''
На вход программе подается натуральное число n>=2 - катет прямоугольного равнобедренного треугольника.
Напишите программу, которая выводит звездный треугольник в соответствии с примером.
'''
n = int(input())
for i in range(n):
    print('*' * n)
    n -= 1