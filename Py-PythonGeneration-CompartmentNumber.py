#В купейном вагоне имеется 999 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 111).
yourplace = int(input())
totalplace = 4
yourkupe = (yourplace + totalplace - 1) // totalplace
print(yourkupe)