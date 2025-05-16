import tkinter as tk
from tkinter import messagebox
from functions import tokenize, add, subtract, multiply, divide

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#f2f2f2")
        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 24), bd=10, relief="flat", justify='right')
        self.display.pack(fill=tk.BOTH, padx=10, pady=20, ipady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            frame = tk.Frame(self.root, bg="#f2f2f2")
            frame.pack(expand=True, fill="both")
            for btn_text in row:
                button = tk.Button(frame, text=btn_text, font=("Arial", 18), bd=0, relief="ridge",
                                   bg="#ffffff", fg="#333333", activebackground="#e6e6e6",
                                   command=lambda b=btn_text: self.on_button_click(b))
                button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                tokens = tokenize(self.expression)
                if not tokens or len(tokens) < 3:
                    raise ValueError("Invalid expression")

                result = tokens[0]
                for i in range(1, len(tokens), 2):
                    operator = tokens[i]
                    next_num = tokens[i + 1]

                    match operator:
                        case '+':
                            result = add(result, next_num)
                        case '-':
                            result = subtract(result, next_num)
                        case '*':
                            result = multiply(result, next_num)
                        case '/':
                            result = divide(result, next_num)
                        case _:
                            raise ValueError(f"Invalid operator '{operator}'")

                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)

            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero.")
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input.\n{e}")
                self.display.delete(0, tk.END)
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
