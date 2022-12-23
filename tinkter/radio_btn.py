from tkinter import *
root = Tk()


def Order():
    dict = {1: "Dosa", 2: "Idli", 3: "Poha"}
    print(f"Your order is {dict[var.get()]}")


root.title("Radiobutton")
root.geometry("800x400")
var = IntVar()
Label(root, text="What would you like to have ?",
      justify=LEFT, padx=14, pady=10, font="comicsans 14 ").pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value=1).pack()
radio = Radiobutton(root, text="Idli", padx=14, variable=var, value=2).pack()
radio = Radiobutton(root, text="Poha", padx=14, variable=var, value=3).pack()
Button(root, text="Order Now", command=Order).pack()
root.mainloop()
