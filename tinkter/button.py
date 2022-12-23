from tkinter import *
root = Tk()


def hello():
    print("Hello Saksham")


root.geometry("800x800")
root.title("Buttons")
f1 = Frame(root, border=None, padx=50, pady=50)
f1.pack(side=LEFT, anchor="nw")
b1 = Button(f1, fg="red", bg="Yellow", text="Print it", command=hello)
b1.pack(side=LEFT, padx=10)

b2 = Button(f1, fg="red", bg="Yellow", text="Print it")
b2.pack(side=LEFT, padx=10)

b3 = Button(f1, fg="red", bg="Yellow", text="Print it")
b3.pack(side=LEFT, padx=10)

b4 = Button(f1, fg="red", bg="Yellow", text="Print it")
b4.pack(side=LEFT, padx=10)

root.mainloop()
