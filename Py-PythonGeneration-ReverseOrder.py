#Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
n1=int(input())
while n1!=0:
    last_n=n1%10
    print(last_n)
    n1//=10