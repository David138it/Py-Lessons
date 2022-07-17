'''
программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.
'''
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
number_of_passwords = int(input('Сколько паролей сгенерировать? '))
length_of_one_password = int(input('Сколько знаков должно быть в пароле? '))
qstn_about_numbers = input('Включать ли цифры 0123456789? да/нет ')
qstn_about_uppercase_alphabet = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет ')
qstn_about_lowercase_alphabet = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет ')
qstn_about_symbols = input('Включать ли символы !#$%&*+-=?@^_ ? да/нет ')
qstn_about_other_symbols = input('Исключать ли неоднозначные символы il1Lo0O ? да/нет ')
chars = ''
if qstn_about_numbers == 'да':
    chars += digits
if qstn_about_uppercase_alphabet == 'да':
    chars += uppercase_letters
if qstn_about_lowercase_alphabet == 'да':
    chars += lowercase_letters
if qstn_about_symbols == 'да':
    chars += punctuation
if qstn_about_other_symbols == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c,'')
def generate_password(len,chars):
    pswrd = ''
    for _ in range(number_of_passwords):
        for _ in range(length_of_one_password):
            pswrd += random.choice(chars)
        pswrd += ' '
    return pswrd
print(generate_password(len, chars))
