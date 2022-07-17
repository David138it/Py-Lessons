'''
Дано натуральное число. Напишите программу, которая вычисляет:
    сумму его цифр;
    количество цифр в нем;
    произведение его цифр;
    среднее арифметическое его цифр;
    его первую цифру;
    сумму его первой и последней цифры.
'''
num=int(input())
total=0
count=0
multiply=1
lastnum=0
firstnum=num%10
while num!=0:
    lastnum=num%10
    num//=10
    total+=lastnum
    count+=1
    multiply*=lastnum
    middle=total/count
totalnum=firstnum+lastnum
print(total,count,multiply,middle,lastnum,totalnum,sep='\n')