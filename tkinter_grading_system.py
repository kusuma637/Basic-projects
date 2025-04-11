import tkinter as tk
from tkinter import messagebox


def calculate_grade():
    try:
        score = float(entry.get())

        if score >= 90:
            grade = "A"
            messagebox.showinfo("Result", f"Congratulations! You have got GRADE: {grade}")
        elif 80 <= score < 90:
            grade = "B"
            messagebox.showinfo("Result", f"Congratulations! You have got GRADE: {grade}")
        elif 70 <= score < 80:
            grade = "C"
            messagebox.showinfo("Result", f"Congratulations! You have got GRADE: {grade}")
        elif 60 <= score < 70:
            grade = "D"
            messagebox.showinfo("Result", f"Congratulations! You have got GRADE: {grade}")
        elif 50 <= score < 60:
            grade = "E"
            messagebox.showinfo("Result", f"Congratulations! You have got GRADE: {grade}")
        elif 0 <= score < 50:
            messagebox.showinfo("Result", "Congratulations! You have FAILED")
        else:
            messagebox.showerror("Error", "Invalid Input: Score must be a non-negative number.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input: Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("300x200")

# Create and place the widgets
label = tk.Label(root, text="Enter your score:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

