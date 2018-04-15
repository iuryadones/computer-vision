from Tkinter import*
import tkMessageBox

def funcao():
	tkMessageBox.showinfo("Curso de Ferias", "Bem Vindo!")



tk = Tk()
frame = Frame(tk)
frame.pack()
btn = Button(frame, text="Entrar")
btn["command"] = funcao
btn["width"] = "20"
btn["height"] = "10"
btn.pack()
#msg = Label(frame, text="Hello World")
#msg.pack()
tk.mainloop()