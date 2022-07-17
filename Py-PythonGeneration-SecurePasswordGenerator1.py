'''
программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.
Подключите модуль random;
Создайте строковые константы:
Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.
Программа должна запрашивать у пользователя следующую информацию:
Количество паролей для генерации;
Длину одного пароля;
Включать ли цифры 0123456789?
Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
Включать ли символы !#$%&*+-=?@^_?
Исключать ли неоднозначные символы il1Lo0O?
'''
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
q1=input('Введите количество паролей для генеации')
q2=input('Введите длину пароля')
q3=input('Включать ли цифры в пароль')
q4=input('Включать ли прописные буквы')
q5=input('Включать ли строчные буквы ')
q6=input('Включать ли символы')
q7=input('Исключать ли неоднозначные символ ')
'''
На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле
'''
if q3 == '+':
    chars=chars+digits
if q4 == '+':
    chars=chars+lowercase_letters
if q5 == '+':
    chars=chars+uppercase_letters
if q6 == '+':
    chars=chars+punctuation
for i in range(int(q1)):
    if q7=='+':
        for i in range(int(q2)):
            if chars.count(chars[i])>1:
                while chars[i]==random.sample(chars):
                    chars.replace(i, random.sample(chars))
    print(*random.sample(chars, int(q2)), sep='')
