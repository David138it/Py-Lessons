'''
Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:
    1
    121
    12321
    1234321
    123454321
    ...
'''
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end='')
    for j in range(i,1,-1):
        print(j-1,end="")
    print("")