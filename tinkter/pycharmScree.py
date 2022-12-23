from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("733x434")

label = Label(text="PyCharm Community Edition", font=('Times', 24))
# photo = PhotoImage(file="PyCharm.png")
# img_label = Label(image=photo, width=300, height=200)
# img_label.pack()

image = Image.open("PyCharm.png")
photo = ImageTk.PhotoImage(image)
# label.pack()

root.mainloop()
