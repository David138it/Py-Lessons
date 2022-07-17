'''
На числовой прямой даны два отрезка: [a1; b1] и [a2; b2]. Напишите программу, которая находит их пересечение.
Пересечением двух отрезков может быть:
    отрезок;
    точка;
    пустое множество.
'''
a1,b1,a2,b2=int(input()),int(input()),int(input()),int(input())
if a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')