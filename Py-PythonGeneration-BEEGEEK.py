'''
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
	число a – должно быть палиндромом;
	число b – должно быть простым;
	число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
'''
def isPrime(n):
    if n % 2 == 0: return(n == 2)
    d = 3
    while d * d <= n and n % d != 0: d += 2
    return(d * d > n)
def isPalindrom(n):
    n = str(n)
    return(n == n[::-1])
def isEven(n): return(not n % 2)
def is_valid_password(password):
    try:
        a, b, c = map(int, password.split(':'))
        return(isPalindrom(a) and isPrime(b) and isEven(c))
    except: return(False)
# считываем данные
psw = input()
# вызываем функцию
print(is_valid_password(psw))
