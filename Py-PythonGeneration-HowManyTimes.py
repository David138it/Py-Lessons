#На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.
st=input()
star = 0
plus = 0
for i in st:
    if i == '*':
        star += 1
    elif i == '+':
        plus += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')