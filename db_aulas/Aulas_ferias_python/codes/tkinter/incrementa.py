from Tkinter import *
def inc():
	n=int(rotulo.configure("text")[4])+1
	rotulo.configure(text=str(n))
b = Button(text="Incrementa",command=inc)
b.pack()
rotulo = Label(text="0")
rotulo.pack()
mainloop()