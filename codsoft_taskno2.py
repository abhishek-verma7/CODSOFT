import tkinter as tk
import random

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("300x350")
        self.window.configure(background="#f0f0f0")  

        self.label = tk.Label(self.window, text="PASSWORD GENERATOR", font=("Helvetica", 18, "bold"), fg="red", bg="#f0f0f0")  
        self.label.pack(pady=10)

        self.number_letter_label = tk.Label(self.window, text="Enter the length of alphabets:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  
        self.number_letter_label.pack()
        self.number_letter_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  
        self.number_letter_entry.pack()

        self.number_digits_label = tk.Label(self.window, text="Enter the length of digits:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  
        self.number_digits_label.pack()
        self.number_digits_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  
        self.number_digits_entry.pack()

        self.number_special_characters_label = tk.Label(self.window, text="Enter the length of symbols:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  
        self.number_special_characters_label.pack()
        self.number_special_characters_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  
        self.number_special_characters_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate Password", command=self.generate_password, font=("Helvetica", 12, "bold"), fg="#fff", bg="blue")  
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.window, text="", font=("Helvetica", 16), fg="#333", bg="#f0f0f0")  
        self.password_label.pack()

    def generate_password(self):
        try:
            number_letter = int(self.number_letter_entry.get())
            number_digits = int(self.number_digits_entry.get())
            number_special_characters = int(self.number_special_characters_entry.get())

            if number_letter < 0 or number_digits < 0 or number_special_characters < 0:
                raise ValueError("Lengths cannot be negative.")

            uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
            lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
            digits = [str(i) for i in range(10)]
            special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_']
            letter = uppercase_letters + lowercase_letters

            password_list = []

            for _ in range(number_letter):
                char = random.choice(letter)
                password_list.append(char)

            for _ in range(number_digits):
                char = random.choice(digits)
                password_list.append(char)

            for _ in range(number_special_characters):
                char = random.choice(special_characters)
                password_list.append(char)

            random.shuffle(password_list)
            password = ''.join(password_list)

            self.password_label.config(text="Your generated password is: " + password)

        except ValueError:
            self.password_label.config(text="Please enter valid lengths (non-negative integers).")

    def run(self):
        self.window.mainloop()

generator = PasswordGenerator()
generator.run()
