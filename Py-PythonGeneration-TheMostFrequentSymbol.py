#На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
string=input()
countSymb=0
symbol=0
for i in string:
    if string.count(i)>=countSymb:
        countSymb=string.count(i)
        symbol=i
print(symbol)