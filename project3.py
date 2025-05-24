import tkinter as tk
from tkinter import messagebox
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def exponentiate(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return a ** 0.5
def sinus(a):
    return math.sin(a)* math.pi / 180  # Convert degrees to radian
def cosinus(a):
    return math.cos(a)* math.pi / 180  # Convert degrees to radian
def tangens(a):
    if a == 90 or a == 270:
        raise ValueError("Cannot take tangent of 90 or 270 degrees.")
    return math.tan(math.radians(a))
def secant(a):
    if a == 90 or a == 270:
        raise ValueError("Cannot take secant of 90 or 270 degrees.")
    return 1 / math.cos(math.radians(a))
def cosecant(a):
    if a == 0 or a == 180:
        raise ValueError("Cannot take cosecant of 0 or 180 degrees.")
    return 1 / math.sin(math.radians(a))


def calculate():
    op = operation_var.get()
    try:
        if op == "√" or op == "sin" or op == "cos" or op == "tan" or op == "sec" or op == "csc":
            a = float(entry_a.get())
            if op == "sin":
                result = sinus(a)
            elif op == "cos":
                result = cosinus(a)
            elif op == "tan":
                result = tangens(a)
            elif op == "sec":
                result = secant(a)
            elif op == "csc":
                result = cosecant(a)
            elif op == "√":
                result = square_root(a)

        else:
            a = float(entry_a.get())
            b = float(entry_b.get())
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            elif op == "^":
                result = exponentiate(a, b)
        result_var.set(f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception:
        messagebox.showerror("Error", "Invalid input.")

def on_operation_change(*args):
    if operation_var.get() == "√" or operation_var.get() in ["sin", "cos", "tan", "sec", "csc"]:
        entry_b.config(state="disabled")
        entry_b.delete(0, tk.END)
    else:
        entry_b.config(state="normal")

root = tk.Tk()
root.title("Simple Calculator")

operation_var = tk.StringVar(value="+")
operation_var.trace_add("write", on_operation_change)

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="Operation:").grid(row=2, column=0)
operations = [("sin", "Sine (sin)"),
                ("cos", "Cosine (cos)"),
                ("tan", "Tangent (tan)"),
                ("sec", "Secant (sec)"),
                ("csc", "Cosecant (csc)"),
                ("+", "Add (+)"), 
                ("-", "Subtract (-)"), 
                ("*", "Multiply (*)"), 
                ("/", "Divide (/)"), 
                ("^", "Exponentiate (^)"),
                ("√", "Square Root (√)")]

# Create a frame to hold radio buttons
op_frame = tk.Frame(root)
op_frame.grid(row=2, column=1, sticky="w")

for val, text in operations:
    tk.Radiobutton(op_frame, text=text, variable=operation_var, value=val).pack(anchor="w")

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=2)

root.mainloop()