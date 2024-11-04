from tkinter import * 
from tkinter import messagebox

def submit():
    student_details = (
        f"Name: {name_val.get()}\n"
        f"Roll No. : {Roll_val.get()}\n"
        f"Phone numnber: {phone_val.get()}\n"
        f"Address: {address_val.get()}\n"
    )

    messagebox.showinfo("Student Details", student_details)

root = Tk()

root.title("Student Details Form")

name = Label(root, text="Name").grid(row=0,column=0)
Roll = Label(root, text="Roll No.").grid(row=1,column=0)
phone = Label(root, text="Phone number").grid(row=2,column=0)
address = Label(root, text="Address").grid(row=3,column=0)

name_val = StringVar()
Roll_val = StringVar()
phone_val = StringVar()
address_val = StringVar()

name_entry = Entry(root, textvariable=name_val).grid(row=0,column=1)
Roll_entry = Entry(root, textvariable=Roll_val).grid(row=1,column=1)
phone_entry = Entry(root, textvariable=phone_val).grid(row=2,column=1)
address_entry = Entry(root, textvariable=address_val).grid(row=3,column=1)

submit_button = Button(root, text="Submit",command=submit).grid(row=4, column=1)


root.geometry("644x460")

root.maxsize(1366,720)
root.minsize(320,320)
root.mainloop()