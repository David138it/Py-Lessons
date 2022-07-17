'''
Напишите программу, которая считывает целое положительное число n, n∈[1; 9] и выводит значение числа n+nn+nnn.
'''
n1=int(input())
desatka=n1*10
sotka=n1*100
n2=n1+desatka
n3=sotka+n2
s=n1+n2+n3
print(s)