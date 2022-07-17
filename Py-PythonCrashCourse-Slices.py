'''
Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
который делает следующее
• Выводит сообщение «The first three items in the list are:», а затем использует срез для
вывода первых трех элементов из списка
• Выводит сообщение «Three items from the middle of the list are:», а затем использует
срез для вывода первых трех элементов из середины списка
• Выводит сообщение «The last three items in the list are:», а затем использует срез для
вывода последних трех элементов из списка
'''
cubes=[i**3 for i in range(1,11)]
print(cubes)
print("The first three items in the list are:")
print(cubes[:3])
print("Three items from the middle of the list are:")
print(cubes[3:6])
print("The last three items in the list are:")
print(cubes[-3:])
