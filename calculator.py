import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
        else:
            result_label.config(text="Select an operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

app = tk.Tk()
app.title("Simple Calculator")

tk.Label(app, text="Number 1:").grid(row=0, column=0)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

tk.Label(app, text="Number 2:").grid(row=1, column=0)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

operation = tk.StringVar(app)
operation.set('+')  # default value

ops_menu = tk.OptionMenu(app, operation, '+', '-', '*', '/')
ops_menu.grid(row=2, column=0, columnspan=2)

calc_button = tk.Button(app, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(app, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

app.mainloop()
