'''
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.
'''
def is_valid_triangle(side1, side2, side3):
    return (side1 < side2 + side3) and (side2 < side3 + side1) and (side3 < side1 + side2)
print(is_valid_triangle(int(input()), int(input()), int(input())))
