

from Tkinter import*
import tkMessageBox

def funcao():
	tkMessageBox.showinfo("Curso de Ferias", "Bem Vindo!")



tk = Tk()
frame = Frame(tk)
frame.pack()


btn = Button(frame, text="b1")
btn.pack(side="right")
btn2 = Button(frame, text="b2")
btn.pack(side="left")
btn2.pack()


tk.mainloop()



