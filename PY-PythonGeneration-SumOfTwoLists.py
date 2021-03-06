'''
На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
Примечание. Количество чисел в обеих строках одинаковое.
Sample Input 1:
На вход программе подаются две строки текста, содержащие целые числа, разделенные символом пробела.
3 1 4
1 5 9
Sample Output 1:
Программа должна вывести текст в соответствии с условием задачи.
4 6 13
'''
l, m = input().split(), input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))
