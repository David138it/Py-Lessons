'''
На вход программе подается натуральное число nn. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2, 5 или 8.
'''
n=int(input())
square=0
summ=0
for i in range(1,n+1):
    square=i**2
    if (square%10==2) or (square%10==5) or (square%10==8):
        summ=summ+i
print(summ)