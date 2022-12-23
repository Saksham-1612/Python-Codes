from tkinter import *


def getavls():
    pass


root = Tk()
root.geometry("800x600")
root.title("Grids and Layouts")

user = Label(root, text="Username")
pswd = Label(root, text="Password")
user.grid()
pswd.grid(row=1)

# entry widget

uservalue = StringVar()
pswdvalue = StringVar()
user_entry = Entry(root, textvariable=uservalue)
pswd_entry = Entry(root, textvariable=pswdvalue)

user_entry.grid(row=0, column=1)
pswd_entry.grid(row=1, column=1)


Button(text="Submit", bg="red", relief=FLAT, command=getavls).grid()
root.mainloop()
