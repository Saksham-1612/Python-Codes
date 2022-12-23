from tkinter import *


def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1


i = 0

root = Tk()
root.geometry("800x400")
root.title("List Box")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First Item")
Button(root, text="AddItem", command=add).pack()
root.mainloop()
