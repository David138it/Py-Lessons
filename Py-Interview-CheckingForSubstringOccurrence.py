#Это маленькая, довольно очевидная подсказка, но я узнал о ней лишь через год изучения Python. 
#Должно быть, вы знаете, что можно проверить, содержится ли нужный элемент в кортеже, списке, словаре, с помощью конструкции 
#'item in list' или 'item not in list'.
string = 'Hi there' # true example
#string = 'Good bye' # false example
if string.find('Hi') != -1:
    print('Success!')
