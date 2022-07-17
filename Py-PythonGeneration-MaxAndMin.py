#Дано натуральное число n, (n>=10). Напишите программу, которая определяет его максимальную и минимальную цифры.
num=int(input())
minimum=9
maximum=0
while num!=0:
    lastnum=num%10
    if lastnum<minimum:
        minimum=lastnum
    if lastnum>maximum:
        maximum=lastnum
    num=num//10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)