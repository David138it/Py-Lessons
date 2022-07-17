'''
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
'''
def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]
n = int(input())
print(get_factors(n))
