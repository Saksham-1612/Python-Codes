from tkinter import *


def mainwindow():

    # $ Main Window GUI
    # *Customer Frame
    root = Tk()
    customerFrame = Frame(root, pady=300, bg="red", padx=210)
    customerFrame.pack(side=LEFT, fill=Y)

    # !Customer Button
    Button(customerFrame, text="Customer", font="Comicsans 15", bg="blue",
           padx=75, pady=75, relief=FLAT).pack(padx=50, fill=Y)

    # *Vendor Frame
    vendorFrame = Frame(root, pady=300, padx=210, bg="green")
    vendorFrame.pack(side=LEFT, fill=Y)

    # !Vendor Button
    Button(vendorFrame, text="Vendor", font="Comicsans 15",
           bg="blue", padx=85, pady=75, relief=FLAT).pack(padx=50, fill=Y)
