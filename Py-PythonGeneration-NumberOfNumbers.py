'''
На вход программе подаются два целых числа a и b (a<=b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.
'''
n1=int(input())
n2=int(input())
counter=0
cube=0
for i in range(n1, n2+1):
    cube=i**3
    if (cube%10==4) or (cube%10==9):
        counter+=1
print(counter)