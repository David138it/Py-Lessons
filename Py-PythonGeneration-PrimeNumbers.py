#На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит все простые числа от a до b включительно.
a=int(input())
b=int(input())
for i in range(a,b+1):
    n=0
    for j in range(1,i):
        if i%j!=0:
            n+=1
        if n==i-2:
            print(i)