'''
Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка (x1;y1) и (x2; y2) и возвращает координаты точки являющейся серединой данного отрезка.
Примечание 1. Координаты середины отрезка вычисляются по формуле: (x1;y1) ((x1+x2)/2;(y1+y2)/2) (x2;y2)
'''
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2
print(*get_middle_point(int(input()), int(input()), int(input()), int(input())))
