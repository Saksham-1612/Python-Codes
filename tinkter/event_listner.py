from tkinter import *


def saksham(event):
    print(("hey this is Saksham"))


root = Tk()
root.geometry("600x400")
root.title("events")
f1 = Frame(root, bg="green")
f1.pack(side=LEFT, padx=50)

f2 = Frame(root, bg="green")
f2.pack(side=LEFT, padx=50)

widget = Button(f1, text="Click me!", fg="#FDF0E0",
                bg="#5837D0", relief=FLAT, pady=30, padx=100)
widget.pack(pady=105)
widget1 = Button(f2, text="Click me!", fg="#FDF0E0",
                 bg="#5837D0", relief=FLAT, pady=30, padx=100)
widget1.pack(pady=105)

widget.bind('<Button-1>', saksham)
widget.bind('<Double-1>', quit)

root.mainloop()
