from Tkinter import *

root = Tk()
w = Label(root, text="Hello world")
w.pack()
quitButton = Button(root, text="sair", command=root.quit)
quitButton.pack()
root.mainloop()