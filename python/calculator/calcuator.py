import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

screen = tk.Entry(root, font=("Arial", 24), borderwidth=2, width=16, relief=tk.RIDGE, justify='right')
screen.pack(fill=tk.X, ipadx=8, ipady=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0

for btn in buttons:
    button = tk.Button(button_frame, text=btn, font=("Arial", 18), relief=tk.RAISED, borderwidth=1, height=2, width=5)
    button.bind("<Button-1>", click)
    button.grid(row=row, column=col, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()