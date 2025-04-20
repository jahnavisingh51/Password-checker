import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    if len(password) < 9:
        return "Weak: At least 9 characters", "red"
    if not any(char.isdigit() for char in password):
        return "Weak: Add at least one digit", "red"
    if not any(char.isupper() for char in password):
        return "Weak: Add at least one uppercase letter", "red"
    if not any(char.islower() for char in password):
        return "Weak: Add at least one lowercase letter", "red"
    if not re.search(r'[!@#$%^&*?(){}<>.]', password):
        return "Medium: Add a special character", "orange"
    return "Strong: Your password is secure!", "green"

def evaluate_password():
    password = entry.get()
    if password.lower() == "exit":
        root.destroy()
        return
    result, color = check_password_strength(password)
    result_label.config(text=result, fg=color)

# Set up the window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Input
entry = tk.Entry(root, width=30, show='*', font=("Arial", 12))
entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check Strength", command=evaluate_password)
check_button.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Run the app
root.mainloop()
