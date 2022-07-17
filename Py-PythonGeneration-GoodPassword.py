'''
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
Пароль является надежным если:
	его длина не менее 88 символов; 
	он содержит как минимум одну заглавную букву (верхний регистр); 
	он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
'''
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])
txt = input()
print(is_password_good(txt))
