import tkinter as tk
from tkinter import messagebox


def calculate_result():
    try:
        # Get student details
        roll = roll_no.get()
        student = name.get()
        dept = department.get()

        if roll == "" or student == "" or dept == "":
            messagebox.showerror("Error", "Please enter all student details")
            return

        # Get marks
        marks = [
            int(math_marks.get()),
            int(dsa_marks.get()),
            int(python_marks.get()),
            int(machine_learning_marks.get()),
            int(Cloud_Computing_marks.get())
        ]

        # Check marks
        if any(mark < 0 or mark > 100 for mark in marks):
            messagebox.showerror(
                "Error",
                "Marks must be between 0 and 100"
            )
            return

        # Calculate total and percentage
        total = sum(marks)
        percentage = total / 5

        # Calculate grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

        # Calculate result
        if all(mark >= 40 for mark in marks):
            result = "PASS"
        else:
            result = "FAIL"

        # Display result
        total_label.config(text=f"Total: {total}/500", bg="lightgray")
        percentage_label.config(
            text=f"Percentage: {percentage:.2f}%",
            bg="lightgray"
        )
        grade_label.config(text=f"Grade: {grade}", bg="lightgray")
        result_label.config(text=f"Result: {result}", bg="lightgray")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid marks"
        )

def clear_data():
    # Clear student details
    roll_no.delete(0, tk.END)
    name.delete(0, tk.END)
    department.delete(0, tk.END)

    # Clear marks
    math_marks.delete(0, tk.END)
    dsa_marks.delete(0, tk.END)
    python_marks.delete(0, tk.END)
    machine_learning_marks.delete(0, tk.END)
    Cloud_Computing_marks.delete(0, tk.END)

    # Clear result
    total_label.config(text="Total: ")
    percentage_label.config(text="Percentage: ")
    grade_label.config(text="Grade: ")
    result_label.config(text="Result: ")


# Main window
root = tk.Tk()
root.title("Student Result Management System")
root.geometry("500x700")


# Title
title = tk.Label(
    root,
    text="STUDENT RESULT MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)


# Student details
tk.Label(root, text="Roll Number").pack()
roll_no = tk.Entry(root)
roll_no.pack(pady=5)

tk.Label(root, text="Student Name").pack()
name = tk.Entry(root)
name.pack(pady=5)

tk.Label(root, text="Department").pack()
department = tk.Entry(root)
department.pack(pady=5)


# Subject marks
tk.Label(root, text="Mathematics").pack()
math_marks = tk.Entry(root)
math_marks.pack(pady=5)

tk.Label(root, text="Data Structure").pack()
dsa_marks = tk.Entry(root)
dsa_marks.pack(pady=5)

tk.Label(root, text="Python").pack()
python_marks = tk.Entry(root)
python_marks.pack(pady=5)

tk.Label(root, text="Machine Learning").pack()
machine_learning_marks = tk.Entry(root)
machine_learning_marks.pack(pady=5)

tk.Label(root, text="Cloud Computing").pack()
Cloud_Computing_marks = tk.Entry(root)
Cloud_Computing_marks.pack(pady=5)

# Buttons
tk.Button(
    root,
    text="Calculate Result",
    command=calculate_result
).pack(pady=15)

tk.Button(
    root,
    text="Clear",
    command=clear_data
).pack(pady=5)


# Result section
tk.Label(
    root,
    text="RESULT",
    font=("Arial", 14, "bold")
).pack(pady=15)

total_label = tk.Label(root, text="Total: ")
total_label.pack(pady=3)

percentage_label = tk.Label(root, text="Percentage: ")
percentage_label.pack(pady=3)

grade_label = tk.Label(root, text="Grade: ")
grade_label.pack(pady=3)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=3)


# Run application
root.mainloop()