from tkinter import *
root = Tk()


def getDollar():
    print(f"Your account is credited with {slider2.get()}$")


root.geometry("800x400")
root.title("Sliders")
Label(root, text="How many dollars you want?").pack()
slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider2.pack()
Button(root, text="Get Dollars", command=getDollar).pack()

root.mainloop()
