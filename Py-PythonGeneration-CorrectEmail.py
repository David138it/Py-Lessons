'''
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
'''
s = input()
if '@' in s and '.' in s:
    print("YES")
else:
    print("NO")