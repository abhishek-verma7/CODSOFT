import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())  # Get desired length of password
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        
        # Generate password
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        
        # Update the password display label
        password_var.set(password)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=20)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

password_display = tk.Label(root, textvariable=password_var, relief="solid", width=30)
password_display.pack()

# Run the main loop
root.mainloop()
