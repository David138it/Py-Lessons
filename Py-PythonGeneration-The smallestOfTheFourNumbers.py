'''
Напишите программу, которая определяет наименьшее из четырёх чисел.
'''
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
if n1 < n2:
    if n3 < n4:
        if n1 < n3:
            print(n1)
        else:
            print(n3)
    else:
        if n1 < n4:
            print(n1)
        else:
            print(n4)
else:
    if n3 < n4:
        if n2 < n3:
            print(n2)
        else:
            print(n3)
    else:
        if n2 < n4:
            print(n2)
        else:
            print(n4) 