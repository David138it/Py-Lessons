'''
Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
'''
n=float(input())
if n==0:
    print("Обратного числа не существует")
else:
    obr=1/n
    print(obr)