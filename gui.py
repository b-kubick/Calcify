import tkinter as tk
import re

# Calculator class that set up the environment and strucutre of the gui
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcify: Calculator")
        self.root.geometry("400x300")  # Set size
        self.root.resizable(False, False)

        self.create_widgets()

# Calculate function that checks if the expression is an evaluator like "+" "-" etc.
    def calculate(self, expression):
        try:
            # Here is where the checker happens
            result = eval(expression)
            if result == float('inf') or result == float('-inf'):
                return "Infinity"
            return result
        except ZeroDivisionError:
            return "Division by zero"
        except Exception as e:
            return str(e)

# Clears the fields
    def clear_entry(self):
        self.entry.delete(0, tk.END)

# Handles button click events
    def on_button_click(self, value):
        current_expression = self.entry.get()
        if value == 'C':
            self.clear_entry()
        elif value == '=':
            # regex match checker for the arithmetic expressions
            if re.match(r'^[\d\s\(\)\+\-\*\/\%\^\.]+$', current_expression):
                result = self.calculate(current_expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            else:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid input")
        else:
            self.entry.insert(tk.END, value)

# Creates layout for calculator gui
    def create_widgets(self):
        self.entry = tk.Entry(self.root, width=20, font=("Roboto", 20), bd=5, relief=tk.GROOVE, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '(', ')', '%'
        ]
        row, col = 1, 0
        for button in buttons:
            action = lambda value=button: self.on_button_click(value)
            tk.Button(self.root, text=button, width=5, height=2, font=("Roboto", 16),
                      command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Make the buttons resize with the window
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    #root.configure(bg="black")
    app = Calculator(root)
    root.mainloop()
