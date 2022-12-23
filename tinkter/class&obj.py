from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.mainloop()
