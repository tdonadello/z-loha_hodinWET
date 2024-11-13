import random
import tkinter as tk
from tkinter import messagebox

def generate_mark():
    student = entry.get()
    if student.lower() == "dony":
        mark_options = [1, 1, 2, 3, 4]
        random_mark = random.choice(mark_options)
    else:
        random_mark = random.randint(1, 5)

    messagebox.showinfo("Result", f"Your mark is: {random_mark}")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Mark Generator")

# Vytvoření vstupního pole
label = tk.Label(root, text="What is your name?")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Tlačítko pro generování známky
button = tk.Button(root, text="Generate Mark", command=generate_mark)
button.pack()

# Spuštění hlavní smyčky
root.mainloop()