from tkinter import *
root = Tk()
root.geometry("1000x400")
root.title("My GUI")

# Label Options
'''text-adds the text
bg-background
fg-foreground
font-sets the font
padx - x padding
font=("comicsans", 20, "bold")
pady - y padding
relief - border style - SUNKEN, RAISED, GROOVE, RIDGE'''

title = Label(text="What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and",
              bg="blue", fg="white", padx=50, pady=20, font="comicsans 9 bold", relief=SUNKEN)

# !Pack options
# ?ANCHOR
# ?title.pack(anchor="nw")
# ?fill
# ?padx
# ?pady
title.pack(side="bottom", anchor="sw", fill=X)
root.mainloop()
