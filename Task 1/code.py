import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    
    # You can add more validation here
    
    if name == "" or email == "" or age == "":
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        messagebox.showinfo("Success", "Registration Successful!\nName: {}\nEmail: {}\nAge: {}\nGender: {}".format(name, email, age, gender))

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5)
age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, padx=10, pady=5)
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=3, column=0, padx=10, pady=5)

# Entry fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

# Radio buttons for gender
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=3, column=1, padx=10, pady=5)
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=3, column=2, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
