#На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
string = input()
if string.endswith('.com') == True or string.endswith('.ru') == True:
    print('YES')
else:
    print('NO')