from Tkinter import *
import tkMessageBox

def displayText():
	""" Display the Entry text value. """
	global entryWidget

	if entryWidget.get() == "":
		tkMessageBox.showerror("Tkinter Entry Widget", "Escreva alguma coisa")
 	else:
 		tkMessageBox.showinfo("Tkinter Entry Widget", "Conteudo =" + entryWidget.get())

if __name__ == "__main__":

 root = Tk()

 root.title("Super Hello World")


# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root)

#Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Escreva seu texto:"
entryLabel.pack()
#entryLabel.pack(side=LEFT)
# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack()
#entryWidget.pack(side=LEFT)

textFrame.pack()

button = Button(root, text="Enviar", command=displayText)
button.pack()

root.mainloop()