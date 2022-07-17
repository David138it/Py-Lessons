'''
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
'''
n1,n2,n3=int(input()), int(input()), int(input())
if (n1>n2 and n1<n3) or (n1>n3 and n1<n2):
    print(n1)
elif (n2>n1 and n2<n3) or (n2>n3 and n2<n1):
    print(n2)
elif (n3>n1 and n3<n2) or (n3>n2 and n3<n1):
    print(n3)