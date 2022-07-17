#Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num1=int(input())
num2=num1%10
answer='YES'
while num1!=0:
    if num2!=num1%10:
        answer='NO'
    num1=num1//10
print(num1,num2,answer)  