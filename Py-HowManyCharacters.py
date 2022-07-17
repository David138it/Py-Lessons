#Подсчет числа символов C в строке
genome = input()
cnt = 0
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print(cnt)