'''
На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
'''
string=input()
if 'хорош' in string.lower():
    print('YES')
else:
    print('NO')