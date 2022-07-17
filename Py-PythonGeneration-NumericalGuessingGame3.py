from random import *
num = randint(1,100)
print('Добро пожаловать в числовую угадайку!\nВведите число от 1 до 100:\n')
'''
Напишите функцию is_valid() в которую передается один строковый аргумент. Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100 и False в противном случае. 
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False
num = input()
print(is_valid(num))
'''
def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100
'''
Организуйте цикл, который будет запрашивать у пользователя данные (цикл может быть бесконечным (while True) или может использовать сигнальную метку с последующим переключением, после угадывания числа);
Запросите у пользователя число от 1 до 100;
Проверьте введенные данные с помощью функции is_valid():
если данные некорректны, выведите текст: 'А может быть все-таки введем целое число от 1 до 100?' и перейдите к следующей итерации основного цикла;
если данные корректны, преобразуйте их к целому числу для удобства дальнейшей работы.
while True: 
    your_number = input('Your number between 1 and 100 is:', )
    if is_valid(your_number) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        number = int(your_number)
        break
'''
def input_num():
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
def compare_num():
    while True:
        n = input_num()
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
compare_num()
