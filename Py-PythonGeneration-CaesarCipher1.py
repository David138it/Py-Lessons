'''
требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
Зашифруйте текст «To be, or not to be, that is the question!» алгоритмом Цезаря с сдвигом вправо на 17 символов.
'''
s = 'To be, or not to be, that is the question!'
new_s = ''
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(s)):
    if s[i].isupper():
        ind = eng_upper_alphabet.find(s[i])
        while not ind + 17 < len(eng_upper_alphabet):
            eng_upper_alphabet += eng_upper_alphabet
        new_s += eng_upper_alphabet[ind + 17]
    elif s[i].islower():
        ind = eng_lower_alphabet.find(s[i])
        while not ind + 17 < len(eng_lower_alphabet):
            eng_lower_alphabet += eng_lower_alphabet
        new_s += eng_lower_alphabet[ind + 17]
    else:
        new_s += s[i]
print(new_s)
