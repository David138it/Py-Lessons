'''
Моя пицца, твоя пицца: начните с программы из упражнения 4-1 Создайте копию
списка с видами пиццы, присвойте ему имя friend_pizzas Затем сделайте следующее
• Добавьте новую пиццу в исходный список
• Добавьте другую пиццу в список friend_pizzas
• Докажите, что в программе существуют два разных списка Выведите сообщение «My
favorite pizzas are:», а затем первый список в цикле for Выведите сообщение «My
friend’s favorite pizzas are:», а затем второй список в цикле for Убедитесь в том, что
каждая новая пицца находится в соответствующем списке
'''
pizzas=['pepperoni','georgian','vegetarian']
for pizza in pizzas:
    #print(pizza)
    print("I like "+pizza+" pizza")
print("\nI really love pizza")
friend_pizzas=pizzas[:]
#print(friend_pizzas)
pizzas.append('cheese pizza')
print("My favourite pizzas are:")
print(pizzas)
friend_pizzas.append('kids pizza')
print("My friend's favourite pizza are:")
print(friend_pizzas)
