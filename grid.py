from tkinter import *

root = Tk()
def myclick():
    mylabel = Label(root, text="Click the button")
    mylabel.pack()
myButton = Button(root, text="I am the Button ", command = myclick(), fg = "red", padx = 30, pady = 25)
myButton.pack()

root.mainloop()
