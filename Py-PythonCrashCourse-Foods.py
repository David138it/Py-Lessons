'''
Больше циклов: во всех версиях foods py из этого раздела мы избегали использования
цикла for при выводе для экономии места Выберите версию foods py и напишите два цикла
for для вывода каждого списка
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
for i in my_foods:
    print(i)
for i in friend_foods:
    print(i)
