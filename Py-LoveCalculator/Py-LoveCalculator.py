from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from random import randint
win=Tk()
#win.iconbitmap("heart.ico")
win.title("Love calculator")
def calculation():
    number=randint(60,100)
    showinfo("Процент любви", f"Это любовь на {number}")
open_img=Image.open("Love_main.png")
render_img=ImageTk.PhotoImage(open_img)
main_image=Label(win,image=render_img)
main_image.image=render_img
main_image.grid(row=0,columnspan=2)
label1=Label(win,text="Enter your name: ", font=("arial",10,"bold"))
label1.grid(row=1,column=0,sticky="w")
entry1=Entry(win,font=("arial",10,"bold"))
entry1.grid(row=1,column=1)
label1=Label(win,text="Enter name your parthers ", font=("arial",10,"bold"))
label1.grid(row=2,column=0)
entry2=Entry(win,font=("arial",10,"bold"))
entry2.grid(row=2,column=1)
button=Button(win,text="Check",font=("arial",12,"bold"),fg='red',bg='black',command=calculation)
button.grid(row=3,columnspan=2)
win.mainloop()
#Source: https://vk.com/wall-76746437_278007?hash=3e593f131fc4b80437
