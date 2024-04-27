import tkinter as tk
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcify: Calculator")
        self.root.geometry("400x300")  # Set size
        self.root.resizable(False, False)

        self.create_widgets()

    def calculate(self, expression):
        """Evaluate the arithmetic expression."""
        try:
            result = eval(expression)
            if result == float('inf') or result == float('-inf'):
                return "Infinity"
            return result
        except ZeroDivisionError:
            return "Division by zero"
        except Exception as e:
            return str(e)

    def clear_entry(self):
        """Clear the entry field."""
        self.entry.delete(0, tk.END)

    def on_button_click(self, value):
        """Handle button click events."""
        current_expression = self.entry.get()
        if value == 'C':
            self.clear_entry()
        elif value == '=':
            if re.match(r'^[\d\s\(\)\+\-\*\/\%\^\.]+$', current_expression):
                result = self.calculate(current_expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            else:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid input")
        else:
            self.entry.insert(tk.END, value)

    def create_widgets(self):
        """Create and layout widgets in the calculator."""
        self.entry = tk.Entry(self.root, width=20, font=("Arial", 20), bd=5, relief=tk.GROOVE, justify=tk.RIGHT)
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
            tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 16),
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
    app = Calculator(root)
    root.mainloop()
