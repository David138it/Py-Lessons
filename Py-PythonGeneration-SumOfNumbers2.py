#На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.
number=int(input())
if number>1000 and number<9999:
    if number%17==0 or number%7==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")