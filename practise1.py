import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("General GUI Template")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter your details:")
label.pack(pady=10)

# Entry
entry_label = tk.Label(root, text="Name:")
entry_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

entry_label = tk.Label(root, text="Phone:")
entry_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Checkbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Subscribe to newsletter", variable=checkbox_var)
checkbox.pack()

# Radio Buttons
label(root, text= "Select the option")
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio1.pack()
radio2.pack()

# Function to display submitted details
def show_details():
    name = name_entry.get()
    subscribed = "Yes" if checkbox_var.get() else "No"
    selected_option = radio_var.get()

    details = f"Name: {name}\nSubscribed: {subscribed}\nSelected Option: {selected_option}"
    messagebox.showinfo("Submitted Details", details)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=show_details)
submit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
