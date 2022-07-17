'''
требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
Текст "Hawnj pk swhg xabkna ukq nqj." был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на n символов. Расшифруйте данный текст. Считайте, что n∈[0;25].
'''
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (65 <= ord(char) <= 90):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif (97 <= ord(char) <= 122):
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif (1040 <= ord(char) <= 1103):
            result += chr((ord(char) + s - 1040) % 66 + 1040)
        else:
            result += char
    return result
text = input()
for s in range(-26, -1):
    print(encrypt(text, s))
