import tkinter as tk
import math

class ScientificCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.attributes("-zoomed", True)  # Make the window full screen
        self.root.resizable(True, True)  # Make the window resizable

        self.entry_value = tk.StringVar()
        self.entry_value.set("0")

        self.entry = tk.Entry(self.root, textvariable=self.entry_value, width=25, font=("Helvetica", 24))
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/', 'sqrt', 'x^2',
            '4', '5', '6', '*', 'sin', 'cos',
            '1', '2', '3', '-', 'tan', 'log',
            '0', '.', '=', '+', 'e', 'pi'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, font=("Helvetica", 18), command=lambda button=button: self.on_click(button)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 5:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text="Clear", width=10, font=("Helvetica", 18), command=self.clear).grid(row=row_val, column=0, columnspan=6, padx=10, pady=10)

    def on_click(self, button):
        current_value = self.entry_value.get()
        if button == '=':
            try:
                result = str(eval(current_value))
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'C':
            self.entry_value.set("0")
        elif button == 'sqrt':
            try:
                result = str(math.sqrt(float(current_value)))
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'x^2':
            try:
                result = str(float(current_value) ** 2)
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'sin':
            try:
                result = str(math.sin(math.radians(float(current_value))))
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'cos':
            try:
                result = str(math.cos(math.radians(float(current_value))))
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'tan':
            try:
                result = str(math.tan(math.radians(float(current_value))))
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'log':
            try:
                result = str(math.log10(float(current_value)))
                self.entry_value.set(result)
            except Exception as e:
                self.entry_value.set("Error")
        elif button == 'e':
            self.entry_value.set(str(math.e))
        elif button == 'pi':
            self.entry_value.set(str(math.pi))
        else:
            if current_value == "0":
                self.entry_value.set(button)
            else:
                self.entry_value.set(current_value + button)

    def clear(self):
        self.entry_value.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculatorApp(root)
    root.mainloop()
