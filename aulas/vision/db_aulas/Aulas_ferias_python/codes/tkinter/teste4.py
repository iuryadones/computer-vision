

from Tkinter import*
import tkMessageBox

def funcao():
	tkMessageBox.showinfo("Curso de Ferias", "Bem Vindo!")



tk = Tk()
frame = Frame(tk)
frame.pack()


label = Label(frame, text="Python")
label.grid(row=1, column= 1)
label2 = Label(frame, text="C")
label2.grid(row=1,column=2)
label3 = Label(frame, text="Assembly")
label3.grid(row=1, column=3)


tk.mainloop()



