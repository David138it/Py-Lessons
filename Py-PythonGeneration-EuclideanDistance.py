'''
На плоскости евклидово расстояние между двумя точками
(x1;y1) и (x2,y2) определяется так p=sqrt((x1-x2)^2+(y1-y2)^2)
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
'''
import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(math.sqrt(((x1 - x2)**2)+((y1 - y2)**2)))