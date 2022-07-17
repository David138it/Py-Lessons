'''
На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
Sample Input:
На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.
William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.
Sample Output:
Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с поясняющим текстом.
Общее количество артиклей: 7
'''
s = input().lower().split()
print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")
