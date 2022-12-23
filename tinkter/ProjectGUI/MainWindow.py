from tkinter import *
from functions import mainwindow
root = Tk()
# Setting Up the full Screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.title("Customer")

# !assiging Variables
nameValue = StringVar()
addressValue = StringVar()
mobileValue = StringVar()
emailValue = StringVar()
pizzaValue = IntVar()

# creating function to store order info


def orderInfo():
    print("Submitting Form")
    global orderId
    orderId = orderId+1
    pizzaType = {1: "Small", 2: "Medium", 3: "Large"}
    pizzaPrice = {1: 95, 2: 195, 3: 295}
    with open("orders.txt", "a") as a:
        a.write(
            f"{orderId,nameValue.get(), addressValue.get(), mobileValue.get(), emailValue.get(),pizzaType[pizzaValue.get()],pizzaPrice[pizzaValue.get()]}\n")


# $functions of diffrent modules
orderId = 0


def CutomerWindow():
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    newWindow = Toplevel(root)
    newWindow.geometry(f"{width}x{height}")
    newWindow.title("Cutomer")

    # ?Order Pizza Frame
    orderPizzaFrame = Frame(newWindow, bg="green", pady=300, padx=110)
    orderPizzaFrame.pack(side=LEFT, fill=Y)

    # ?Cancel Order Frame
    cancelOrderFrame = Frame(newWindow, bg="red", pady=300, padx=110)
    cancelOrderFrame.pack(side=LEFT, fill=Y)

    # ?Track Order Frame
    trackOrderFrame = Frame(newWindow,  bg="yellow", pady=300, padx=110)
    trackOrderFrame.pack(side=LEFT, fill=Y)

    # !Button for Order Pizza
    Button(orderPizzaFrame, text="Order Pizza", font="Comicsans 15",
           bg="blue", padx=70, pady=70, relief=FLAT, command=orderPizza).pack(padx=20, fill=Y)

    # !Button for Cancel Order
    Button(cancelOrderFrame, text="Cancel Order", font="Comicsans 15",
           bg="blue", padx=70, pady=70, relief=FLAT, command=cancelOrder).pack(padx=20, fill=Y)

    # !Button for Track Order
    Button(trackOrderFrame, text="Track Order", font="Comicsans 15",
           bg="blue", padx=70, pady=70, relief=FLAT).pack(padx=20, fill=Y)


def orderPizza():
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    newWindow = Toplevel(root)
    newWindow.geometry(f"{width}x{height}")
    newWindow.title("Order Pizza")
    frame = Frame(newWindow, padx=500)

    # !order Pizza Label
    Label(frame, text="Order Pizza", fg="blue", font="Comicsans 22").grid(
        row=0, column=0, columnspan=2, pady=(200, 20))
    # $Name
    Label(frame, text="Name", font="comicsans 15",).grid(
        row=1, column=0, pady=2, sticky='w', padx=(0, 15))

    Entry(frame, font="comicsans 15", relief=FLAT, bg="#f1e740", textvariable=nameValue).grid(
        row=1, column=1, sticky='e')

    # $Address
    Label(frame, text="Address", font="comicsans 15").grid(
        row=2, column=0, pady=2, sticky='w', padx=(0, 15))
    Entry(frame, font="comicsans 15", relief=FLAT, bg="#f1e740", textvariable=addressValue).grid(
        row=2, column=1, sticky='e')

    # $Mobile Number
    Label(frame, text="Mobile Number", font="comicsans 15").grid(
        row=4, column=0, pady=2, sticky='w', padx=(0, 15))
    Entry(frame, font="comicsans 15", relief=FLAT, bg="#f1e740", textvariable=mobileValue).grid(
        row=4, column=1, sticky='e')

    # $Email ID
    Label(frame, text="Email ID", font="comicsans 15").grid(
        row=5, column=0, pady=2, sticky='w', padx=(0, 15))
    Entry(frame, font="comicsans 15", relief=FLAT, bg="#f1e740", textvariable=emailValue).grid(
        row=5, column=1, sticky='e')

    # $Radio buttons for Pizza Type
    Label(frame, text="Pizza Type",
          justify=LEFT, font="comicsans 14 ").grid(row=6, column=0, sticky="w", pady=2)
    radio = Radiobutton(frame, text="Small @95", font="comicsans 12",
                        variable=pizzaValue, value=1).grid(row=6, column=1, sticky="w")
    radio = Radiobutton(frame, text="Medium @195", font="comicsans 12",
                        variable=pizzaValue, value=2).grid(row=6, column=1, sticky="w", padx=(110, 0))
    radio = Radiobutton(frame, text="Large @290", font="comicsans 12",
                        variable=pizzaValue, value=3).grid(row=6, column=2, sticky="w")

    #!Button
    # Create cancel button
    button = Button(frame, text="Order Now",
                    font="comicsans 15", relief=FLAT, bg="blue", command=orderInfo)
    button.grid(column=0, row=7, columnspan=2, pady=10)
    frame.pack()


def cancelOrder():
    # Add width and height of the newWindow
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    newWindow = Toplevel(root)
    newWindow.geometry(f"{width}x{height}")
    newWindow.title("Cancel Order")

    # Create Frame
    frame = Frame(newWindow, pady=300)
    frame.pack()

    # Create a label for Name
    name_label = Label(frame, text="Name:", font="comicsans 15")
    name_label.grid(column=0, row=0, sticky='w')
    # Create an entry for Name
    name_entry = Entry(frame, bd=1, font="comicsans 15")
    name_entry.grid(column=1, row=0, sticky='e')

    # Create a label for order
    order_label = Label(frame, text="Order ID:", font="comicsans 15")
    order_label.grid(column=0, row=1, sticky='w')
    # Create an entry for order
    order_entry = Entry(frame, bd=1, font="comicsans 15")
    order_entry.grid(column=1, row=1, sticky='e')

    # Create cancel button
    button = Button(frame, text="Cancel Now",
                    font="comicsans 9 bold", width=30, bg="blue")
    button.grid(column=1, row=2, sticky='e')


def mainwindow():

    # $ Main Window GUI
    # *Customer Frame
    customerFrame = Frame(root, pady=300, bg="red", padx=210)
    customerFrame.pack(side=LEFT, fill=Y)

    # !Customer Button
    Button(customerFrame, text="Customer", font="Comicsans 15", bg="blue",
           padx=75, pady=75, relief=FLAT, command=CutomerWindow).pack(padx=50, fill=Y)

    # *Vendor Frame
    vendorFrame = Frame(root, pady=300, padx=210, bg="green")
    vendorFrame.pack(side=LEFT, fill=Y)

    # !Vendor Button
    Button(vendorFrame, text="Vendor", font="Comicsans 15",
           bg="blue", padx=85, pady=75, relief=FLAT).pack(padx=50, fill=Y)


mainwindow()
root.mainloop()
