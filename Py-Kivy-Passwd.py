#Алгоритм работы
#1) импортируем нужные библиотеки
from tkinter import * #1
from tkinter import messagebox #2 высплывающие окна сообщений
import pickle#40
#2) Отрисовываем окно
root=Tk()#3
root.geometry("300x500")#4 создание окна
root.title("Vhod")#5
#3) Создаем функцию регистрация
def registration():#7
    text=Label(text="Dliya vhoda v sistemu zaregaites")#8
    text_log=Label(text="Vvedite Vash login: ")#9 Мы должны понять, что будет вводиться Логин
    registr_login=Entry()#10 Теперь вводим логин
    text_password1=Label(text="Vvedite Vassh parol: ")#11
    registr_password1=Entry()#12 Теперь нужно ввести наш пароль, но при этом нам не нужно, чтоб мы видели, что мы вводим пароль
    text_password2 = Label(text="Vvedite eshe raz parol: ")#13
    registr_password2 = Entry(show="*")#14
    button_regist=Button(text="Zaregatsiya", command=lambda: save())#15 Сделаем кнопку реегистрации #48 нужно, чтоб эта функция save работала при нажатии на Зарегестрироваться, поэтому делаем анонимную функцию и вызываем функцию save
    #49 Появвилось окошко при нажатии Зарегестрироваться, но пока что это окошко не рабочее
    text.pack()#16 Расставить все красиво
    text_log.pack()#17
    registr_login.pack()#18
    text_password1.pack()#19
    registr_password1.pack()#20
    text_password2.pack()#21
    registr_password2.pack()#22
    button_regist.pack()#23
#5) Создаем функцию, которая сохранит наши зарегистрированные данные
    def save():#41
        login_pass_save={}#42 Нужно создать переменную, которая создаст массив или словарь
        login_pass_save[registr_login.get()]=registr_password1.get()#43 Теперь нужно сохранить то, что мы ввели
        f=open("Py-Kivy-PasswdLog.txt", "wb")#44 Создадим документ, в котором это будет храниться
        pickle.dump(login_pass_save, f)#45 Мы сохраняем наш логин в введенный текст
        f.close#46 Закрываем этот файл
        login()#47 и вызываем функцию логин
#4) Создаем функцию вход в систему
def login():#25
    text_log=Label(text="Posdravliyam! Teper vi mojete voiti v sistemu")#26
    text_enter_login=Label(text="vvedite Vash login")#27
    enter_login=Entry()#28
    text_enter_pass=Label(text="Vedite vash parol")#29
    enter_password=Entry(show="*")#30
    button_enter=Button(text="voiti", command=lambda: log_pass())#31 #58 funkciya log_pass doljna rabotat pri klike voiti
    text_log.pack()#32
    text_enter_login.pack()#33
    enter_login.pack()#34
    text_enter_pass.pack()#35
    enter_password.pack()#36
    button_enter.pack()#37
#6) Создаем функцию проверки правильности введенного пароля
    def log_pass(): #50
        f=open("Py-Kivy-PasswdLog.txt", "rb")#51 Мы должны открыть тот файл, в котором сохранились наши данные
        a=pickle.load(f)#52 Мы должны создать переменную A, которая будет выгружать (load) наши данные
        f.close()#53 Теперь наш файл нам не нужен, мы это можем закрыть
        if enter_login.get() in a:#54 Сделаем проверку, есть ли такой логин в выгруженном словаре A, то есть если наше введенное имя "enter_login" соответствует словарю A
            if enter_password.get()==a[enter_login.get()]:#55 То если наш пароль enter_password будет равнов списке A паролю в выгруженном файле
                messagebox.showinfo("Privet, u tebiya 5 novih soobsheni")#56 То мы выводим окошко
            else:
                messagebox.showerror("oshibka, vi vveli neverni login")#57 
        else:
            messagebox.showerror("oshibka, vi vveli neverni login")#57 иначе ошибка
registration()#24 проверим
#39login()#38 Проверим
root.mainloop()#6 Запуск окна, на экране появится пустое окно




