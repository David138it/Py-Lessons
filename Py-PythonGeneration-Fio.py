#На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу, которая выводит инициалы человека.
symbol=''
for i in range(3):
    fio=input()
    symbol+=fio[0]
    #print(i,fio, symbol)
print(symbol[1]+symbol[0]+symbol[2])