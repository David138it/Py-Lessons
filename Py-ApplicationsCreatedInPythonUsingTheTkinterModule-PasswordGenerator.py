#Source: https://www.youtube.com/playlist?list=PL9aGGxgLOVw44btcB1CM6j_jhrl7L95aH
from tkinter import *
from random import choice
def randomize():
	lengthPassword=e.get()
	e.delete(0, END)
	for i in range(int(lengthPassword)):
		e.insert(0, choice(alphabet))
root=Tk()
root.title('Password generarot')
root.geometry('200x100')
root.resizable(width=False,height=False)
alphabet=['1','2','3','4','5','6','7','8','9',
	'q','w','e','r','t','y','u','i','o','p',
	'a','s','d','f','g','h','k','l','z','x',
	'c','v','b','n','m','Q','W','E','R','T',
	'Y','U','I','O','P','A','S','D','F','G',
	'H','J','K','L','Z','X','C','V','B','N',
	'M','_','-','.','@']
e=Entry(root,font='Arial 13')
e.place(relx=0.5,y=20,anchor=CENTER)
btn=Button(root,text='Generate',font=('Comic Sans MS', 17, 'bold'), command=randomize)
btn.place(relx=0.5,y=70,anchor=CENTER)
root.mainloop()
