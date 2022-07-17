#Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+...+n!.
n=int(input())
summ=0
for i in range(1,n+1):
    fact=1
    for j in range(1, i+1):
        fact*=j
    summ+=fact
print(summ)