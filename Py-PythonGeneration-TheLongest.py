'''
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.
Sample Input:
На вход программе подается строка текста.
проспал почти всю ночь
Sample Output:
Программа должна вывести текст в соответствии с условием задачи.
7
'''
print(max([len(a) for a in input().split()]))
