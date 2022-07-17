'''
Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. При смешивании двух основных цветов получается вторичный цвет:
    если смешать красный и синий, то получится фиолетовый;
    если смешать красный и желтый, то получится оранжевый;
    если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который получится в результате.
'''
color1, color2 = input(), input()
if color1 == 'красный' and color2 == 'синий' or (color1 == 'синий' and color2 == 'красный'):
    print('фиолетовый')
elif color1 == 'желтый' and color2 == 'синий' or (color1 == 'синий' and color2 == 'желтый'):
    print('зеленый')
elif color1 == 'красный' and color2 == 'желтый' or (color1 == 'желтый' and color2 == 'красный'):
    print('оранжевый')
elif color1 == 'красный' and color2 == 'красный' or color1 == 'желтый' and color2 == 'желтый' or color1 == 'синий' and color2 == 'синий':
    print(color1)
else:
    print('ошибка цвета')