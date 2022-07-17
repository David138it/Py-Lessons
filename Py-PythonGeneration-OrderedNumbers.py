#Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
num=int(input())
answer='YES'
while num//10!=0 :
    lastnum=num%10  
    num=num//10
    if lastnum>num%10:
        answer='NO'
    print(lastnum,num,answer)