'''
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
    1−2+3−4+5−6+...+(−1)^(n+1)*n
'''
n=int(input())
s=0
for i in range(n+1):
    if i%2==0:
        s-=i
    else:
        s+=i
print(s)