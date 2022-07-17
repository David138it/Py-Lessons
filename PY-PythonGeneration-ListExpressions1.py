# получить список всех чисел палиндромов от 100 до 1000.
palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
print(palindromes)
