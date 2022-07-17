'''
Шведский стол: меню «шведского стола» в ресторане состоит всего из пяти пунктов
Придумайте пять простых блюд и сохраните их в кортеже
• Используйте цикл for для вывода всех блюд, предлагаемых рестораном
• Попробуйте изменить один из элементов и убедитесь в том, что Python отказывается
вносить изменения
• Ресторан изменяет меню, заменяя два элемента другими блюдами Добавьте блок
кода, который заменяет кортеж, и используйте цикл for для вывода каждого элемента
обновленного меню
'''
dishes=('Lingonberry jam for cutlets','Pickled herring','Crusty bread','Shrimp sandwich','Pea soup and pancakes')
for i in dishes:
    print(i)
#dishes[1]='Princess Cake'
#print(dishes)
print("")
dishes=('Lingonberry jam for cutlets','Princess Cake','Crusty bread','Shrimp sandwich','Sweet holiday')
for i in dishes:
    print(i)
