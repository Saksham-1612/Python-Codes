from tkinter import *
import tkinter.messagebox as tmsg


def myfunc():
    print("hey there")


def help():
    print("i will help")
    tmsg.showinfo("help", "Saksham here")
    # tmsg.showinfo("help", "Saksham here")


def rate():
    print("rate us")
    value = tmsg.askquestion("feedback", "How was your experience ?")
    print(value)


root = Tk()
root.geometry("800x400")
root.title("Pycharm")
mymenu = Menu()
# use these to create non drop down
frames.pymymenu.add_command(label="file", command=myfunc)
mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


# filemenu = Menu(root)
# m1 = Menu(filemenu, tearoff=0)
# m1.add_command(label="Save", command=myfunc)
# m1.add_command(label="Save as", command=myfunc)
# m1.add_command(label="Print", command=myfunc)
# root.config(menu=filemenu)
# filemenu.add_cascade(label="file", menu=m1)


# m2 = Menu(filemenu, tearoff=0)
# m2.add_command(label="Help", command=help)
# m2.add_command(label="Rate", command=rate)
# root.config(menu=filemenu)
# filemenu.add_cascade(label="Help", menu=m2)
# root.mainloop()
