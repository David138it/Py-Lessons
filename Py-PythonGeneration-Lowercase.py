'''
На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
'''
string=input()
count=0
for i in range(len(string)):
    #print(string[i])
    '''if (string[i]==string[i].lower()):
        count+=1
        #print(string[i],count,i)'''
    if (string[i] in '0123456789'):
        continue
    elif (string[i]==string[i].lower()):
        count+=1
print(count)