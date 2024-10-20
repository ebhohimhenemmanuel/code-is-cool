import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    strength = "Weak"
    
    if len(password) >= 8:
        strength = "Medium"
    if len(password) >= 12:
        strength = "Strong"
    
    messagebox.showinfo("Password Strength", f"Your password strength is: {strength}")

app = tk.Tk()
app.title("Password Strength Checker")

label = tk.Label(app, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(app, show='*')
entry.pack(pady=10)

button = tk.Button(app, text="Check Strength", command=check_password_strength)
button.pack(pady=20)

app.mainloop()
