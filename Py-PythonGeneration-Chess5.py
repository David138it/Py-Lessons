#Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):#слон
    print('YES')
elif (x1==x2 or x2==x1+1 or x2==x1-1) and (y1==y2 or y2==y1+1 or y2==y1-1): #король
    print('YES')
elif x1==x2 or y1==y2:#ладья
    print('YES')
else :
    print('NO')