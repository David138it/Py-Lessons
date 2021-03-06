'''
На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 
Sample Input:
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
4 5 1 2 3 8
Sample Output:
Программа должна вывести две строки текста в соответствии с условием задачи.
1 2 3 4 5 8
8 5 4 3 2 1
'''
n = input().split()   #считываем данные
for i in range(len(n)):     #запускаем цикл
    n[i] = int(n[i])        #преобразуем строковые данные в цифровые
n.sort()              #сортируем список
print(*n)             #выводим на печать 1-ую строку
n.sort(reverse=True)  #переворачиваем отсортированный список
print(*n)             #выводим на печать 2-ую строку
