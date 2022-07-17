'''
Геометрической прогрессией называется последовательность чисел b1,b2,…,bn, каждое из которых, начиная с b2, получается из предыдущего умножением на одно и то же постоянное число q (знаменатель прогрессии), то есть
    bn=b(n−1)*q
Если известен первый член прогрессии и её знаменатель, то n-ый член геометрической прогрессии находится по формуле
    bn=b1*q^(n−1)
'''
b1=int(input())
q=int(input())
n=int(input())
print(b1*q**(n-1))