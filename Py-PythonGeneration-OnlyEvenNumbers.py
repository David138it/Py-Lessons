'''
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
'''
flag='YES'
for i in range(1,11):
    n=int(input())
    if n%2!=0:
        flag='NO'
print(flag)