from tkinter import *
from tkinter import messagebox

# Function for menu commands
def show_message(item):
    messagebox.showinfo("Menu Selection", f"You selected {item}")

# Main window
root = Tk()
root.title("Menu Bar Demonstration")
root.geometry("500x300")

# Menu bar
menubar = Menu(root)

# File Menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: show_message("New"))
file_menu.add_command(label="Open", command=lambda: show_message("Open"))
file_menu.add_command(label="Save", command=lambda: show_message("Save"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: show_message("Cut"))
edit_menu.add_command(label="Copy", command=lambda: show_message("Copy"))
edit_menu.add_command(label="Paste", command=lambda: show_message("Paste"))
menubar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_message("About"))
menubar.add_cascade(label="Help", menu=help_menu)

# Display menu bar
root.config(menu=menubar)

# Heading
label = Label(
    root,
    text="Menu Bar Demonstration",
    font=("Arial", 16, "bold")
)
label.pack(pady=100)

root.mainloop()