from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Frames")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
l1 = Button(f1, text="project tk - Notepad")
l1.pack(pady=50)
f2 = Frame(root, bg="red", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill=X)
l2 = Label(f2, text="Sublime")
l2.pack()
root.mainloop()
