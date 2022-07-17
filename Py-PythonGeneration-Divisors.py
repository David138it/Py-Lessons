'''
На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
'''
a, b = int(input()), int(input())
counter = 0 # счетчик подсчета суммы делителей
number = 1 # число которое будем выводить (минимум 1)
summa = 0  # тут будет сумма делителей, которую надо будет вывести
for i in range(a, b + 1):  # проверяем каждое число в [a;b]
    counter = 0 # обнуляем счетчик для каждого i
    for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
        if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
            counter += j  # создаем сумму делителей
    if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
        summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
        number = i  # число у которого делителей оказалось больше, теперь равно number
print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей