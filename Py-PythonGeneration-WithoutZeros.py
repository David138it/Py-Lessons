'''
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
'''
result=1
for i in range(10):
    n=int(input())
    if n==0:
        n+=1
    result*=n
print(result)