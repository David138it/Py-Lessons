#Блокнот
#1) Импортируем нужные библиотеки
from tkinter import * #1
from tkinter import messagebox #2
from tkinter.filedialog import askopenfile, asksaveasfile #3
#3) Создаем нужные функции
#a) Новый файл
file_name=NONE#12 Зададим параметры без имени
def new_file():#13 Создадим функцию файл меню
    global file_name#14 объявляем глобальную переменную file_name
    file_name="Bez nazvaniya"#15 Изначально file_name будет без названия
    text.delete('1.0', END)#17 Изначально, мы удаляем все, что нам когда то пригодится в заметках, 1.0 - это то где мы удаляем и все остальное вставляем в конец нашего списка
#b) Сохранить как
def save_as():#17
    out=asksaveasfile(mode='w', defaultextension='.txt')#18 Запишим наши файлы и еще вызываем спец окошко
    data=text.get('1.0', END)#19 заставим это все работать
    try:#20 Теперь нужно предовратить ошибку или вызвать ee. Если мы что то записали, то мы сохраняем. а если не можем сохранить, то должна появиться ошибка
        out.write(data.rstrip())#21  если можно записать файл
    except Exception: #22 Дальше мы должны вывести ошибку, если что
        messagebox.showerror("Kelzaya sohranit fail") #23
#d) Открыть файл
def open_file():#24
    global file_name#25 Так как, изначально имени не должно быть, пишем глобальную переменную
    inp=askopenfile(mode='r')#26 Мы должны вызвать наш open fail
    if inp is None:#27 Если мы открываем наш файл, то, изначально, надо будет удалить из нашего файла, когда мы открываем его
        return#28
        file_name=inp.name#29
    data=inp.read() #30 Чтоб мы могли прочитать это 
    text.delete('1.0', END)#31 потом удаляем все из нашего файла
    text.insert('1.0', data)#32

root=Tk() #4
root.title("Zametki") #5
root.geometry("400x400") #6
#2) Создаем окно с менюбаром
text=Text(root, width=400, height=400)#16
text.pack()#16
menu_bar=Menu(root)#8
file_menu=Menu(menu_bar)#9 создадим переменную, которая отвечает за файл меню

file_menu.add_command(label="Hovi", command=new_file)#33 Теперь на на каждую функцию, нужно делать всплывающее окно.
file_menu.add_command(label="Otkrit", command=open_file)#34 Теперь на на каждую функцию, нужно делать всплывающее окно.
file_menu.add_command(label="Sohranit kak", command=save_as)#35 Теперь на на каждую функцию, нужно делать всплывающее окно.

menu_bar.add_cascade(label="Fail", menu=file_menu)#10 красиво все расставим на экранне
root.config(menu=menu_bar)#11 Ставим это в окошко,и у нас на экране должно появиться  пустой меню файл.
root.mainloop() #7

#c) Сохранить





