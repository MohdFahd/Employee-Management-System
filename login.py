import tkinter as tk
from tkinter import messagebox
import subprocess

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin123":
        # Successful login, open the main page
        root.destroy()  # Close the login window
        open_main_page()
    else:
        # Failed login, show an error message
        messagebox.showerror("Login Error", "Invalid username or password")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

def open_main_page():
    # Add your main page functionality here
    subprocess.run(["python", "E:\\python_codes\\ui_project\\Employee-Management-System\\main.py"])

def close_window():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Center the window on the screen
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)




# Create and place widgets
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

close_button = tk.Button(root, text="Close", command=close_window)
close_button.grid(row=2, column=2, pady=20)
# Run the Tkinter event loop
root.mainloop()
