from tkinter import *
root = Tk()

root.geometry("500x500")


def store():
    print("Submitting Form")
    with open("records.txt", "w") as a:
        a.write(
            f"{name_value.get(), phone_value.get(), gender_value.get(), payment_value.get()}")


# heading
l1 = Label(root, text="Welcome to Travels",
           font="somisans 13 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
payment = Label(root, text="payment")


name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
payment.grid(row=4, column=1)

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
payment_value = StringVar()
food_service = IntVar()

name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
payment_entry = Entry(root, textvariable=payment_value)
foodservice_entry = Entry(root, textvariable=food_service)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
payment_entry.grid(row=4, column=3)

food_service = Checkbutton(
    text="Prebook meal?", variable=food_service, relief=FLAT)
food_service.grid(row=6, column=3)

Button(text="Submit", command=store).grid(row=7, column=3)
root.mainloop()
