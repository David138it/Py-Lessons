'''
На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.
Примечание 1. Для вывода элементов списка используйте цикл for.
Примечание 2. Используйте метод split().
Sample Input 1:
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
2 4 3
Sample Output 1:
Программа должна вывести текст в соответствии с условием задачи.
8 64 27
'''
print(*[int(i) ** 3 for i in input().split()])
