

from Tkinter import*
import tkMessageBox

def funcao():
	tkMessageBox.showinfo("Curso de Ferias", "Bem Vindo!")



tk = Tk()
frame = Frame(tk)
frame.pack()


label = Label(frame, text="python")
label["font"] = ("Arial", 25)
label.pack()



tk.mainloop()



