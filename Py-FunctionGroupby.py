'''
Выводим повторяющиеся элементы и количество их повторений
Функция groupby() позволяет получить повторяющиеся элементы в итераторе и сгруппировать их.
'''
from itertools import groupby
for key, group in groupby('Pytttthhhhhonissssst'):
    print(key, list(group))
