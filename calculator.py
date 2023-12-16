import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x500")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = ttk.Entry(self, textvariable=self.result_var, font=('Helvetica', 18), justify="right")
        entry.grid(row=0, column=0, columnspan=6, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("π", 5, 2), ("C", 5, 3),
            ("%", 6, 0), ("√", 6, 1), ("³√", 6, 2), ("quit", 6, 3),
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                expression = self.result_var.get()
                expression = expression.replace("^", "**")
                expression = expression.replace("π", "math.pi")
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == "C":
            self.result_var.set("")
        elif value == "quit":
            self.quit()
        elif value == "%":
            try:
                expression = self.result_var.get()
                result = eval(expression) / 100
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == "√":
            try:
                expression = self.result_var.get()
                result = math.sqrt(eval(expression))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == "³√":
            try:
                expression = self.result_var.get()
                result = eval(expression) ** (1/3)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + str(value))

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
