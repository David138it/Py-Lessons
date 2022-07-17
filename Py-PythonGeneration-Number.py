#На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки
number=input()
summ=0
for i in range(len(number)):
    summ+=int(number[i])
    #print(i,summ,len(number),int(number[i]))
print(summ)