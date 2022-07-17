'''
Напишите программу, которая упорядочивает три числа от большего к меньшему.
'''
n1,n2,n3=int(input()),int(input()),int(input())
print(max(n1,n2,n3))
print(n1 + n2 + n3 - min(n1,n2,n3) - max(n1,n2,n3))
print(min(n1,n2,n3))