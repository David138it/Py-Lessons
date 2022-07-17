from kivy.app import App #1-6 простейший макет Киви
from kivy.uix.button import Button #10-12 Добавим Виджеты кнопок
from kivy.uix.widget import Widget #11 Пустой виджет добавляем
from kivy.uix.label import Label #14 Добавим поле, которое выодит результат
from kivy.uix.gridlayout import GridLayout #7 Нам понадобятся таблицы, чтоб ввести эти буквы, поэтому пишем gridloyaout
from kivy.uix.boxlayout import BoxLayout#15 Так как нам нужно добавить поле снизу вверх, значит в ГридЛайот добавлять нельзя, а значит нам так же понадобится Бокслайот
#from kivy.uix.anchorlayout import AnchorLayout #24 мы хотим тест в поле расположить слева, по 9ти сторонам можетрасположить только anchorlayout
from kivy.config import Config#20
Config.set('graphics','resizable',0)#21
Config.set('graphics','width',400)#22 Ширина окна
Config.set('graphics','height',500)#23 Высота окна
class CalculatorApp(App): #2
    def update_label(self): #43
        self.lbl.text=self.formula #44
    def add_number(self, instance): #32 Создадим функцию, которая создает события
        if(self.formula=="0"):#38 если формула = 0
            self.formula="" #39 тогда очишается и вбивается заново, это нужно для того чтобы не отображать текущий ноль
        self.formula += str(instance.text) #35
        #print(self.formula)#36 Выведем в консоль чтоб посмотреть как это выглядит
        #37 на окне когда мы нажимаем на цифру, эта цифра выводится на консоле 
        self.update_label()#42
    def add_operation(self, instance):#40 Создаем метод который назовем add_operation, для того чтоб прога понимала, что мы нажимаем на операции 
        if(str(instance.text).lower()=="x"):#43 замена при нажатии Х, на *
            self.formula += "*"#43
        else:
            self.formula += str(instance.text)#41#43
        self.update_label()#42
    def calc_result(self, instance): #44
        self.lbl.text=str(eval(self.lbl.text)) #45
        self.formula="0" #46 чтоб очистить потом результат
    def build(self): #3
        #pass #4
        self.formula="0" #34 оздадим переменную формула
        bl=BoxLayout(orientation='vertical', padding=25)#16 создаем БоксЛайот и сразу создаем ему позицию - вертикальную
        gl=GridLayout(cols=4, spacing=3, size_hint=(1, .6)) #8 Создаем GridLayout, создаем колонны
        #al=AnchorLayout(anchor_x="right", anchor_y="center", size_hint=(1, .4)) #25
        #bl.add_widget(Label(text="0", font_size=40, halign="right", size_hint=(1, .4))) #17 сразу добавляем виджет лэйбел
        #self.lbl.=Label(text="0", font_size=40, halign="right", size_hint=(None, None), size=(40*5,40)) #27 пропишем метод селв, чтоб в дальнейшим с ним работать
        self.lbl=Label(text="0", font_size=40, halign="right", valign="center", size_hint=(1, .4), text_size=(400-50, 500* .4-50)) #30 AnchorLayout нам не понадоиблся, поэтому убираем его увеличисваем ширину текста что б сдвинуть влево текст
        #al.add_widget(self.lbl)#28
        #bl.add_widget(al) #29 Этот виджет добавляем в ancorloayt
        bl.add_widget(self.lbl)#31
        gl.add_widget(Button(text="7", on_press=self.add_number))#12 Добавим Виджеты кнопок. 33 добавляем функионал
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="X", on_press=self.add_operation))

        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="-", on_press=self.add_operation))

        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="+", on_press=self.add_operation))

        gl.add_widget(Widget()) #13 пустой Виджет
        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text=".", on_press=self.add_number))
        gl.add_widget(Button(text="=", on_press=self.calc_result))

        #return gl #9 Возвращаем GridLayout
        bl.add_widget(gl) #19 перед возвратом BoxLayout добавим в GridLayout
        return bl #18 Возвращаем BoxLayout
if __name__ == "__main__": #5
    CalculatorApp().run() #6
