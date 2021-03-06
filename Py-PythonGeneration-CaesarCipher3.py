'''
требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
Текст "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd." был получен в результате шифрования алгоритмом Цезаря со сдвигом вправо на 2525 символов. Расшифруйте данный текст.
'''
n, s = -25, 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
for i in s:
    if i.isalpha():
        c = ('a', 'A')[i.isupper()]
        print(chr(ord(c) + (ord(i) + n - ord(c)) % 26), end='')
    else:
        print(i, end='')
