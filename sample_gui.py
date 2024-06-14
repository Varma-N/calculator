from tkinter import *
root = Tk()
root.title("Calculator")


def button_data(num):
    entry.insert(END,num)

def clear():
    entry.delete(0, END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "Math error")
    except SyntaxError:
        entry.delete(0, END)
        entry.insert(END, "Syntax error")
entry = Entry(root, width=30, borderwidth=10)
entry.grid(row=0,column=0, columnspan=4, padx=(0,50), pady=10)
buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
           ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("0", 4, 0), (". ", 4, 1), ("+", 4, 3)]
for (num, r, c) in buttons:
    button = Button(root, text=num, padx=20, pady=10, command=lambda n=num:button_data(n))
    button.grid(row=r, column=c,padx=5,pady=5)

Button(root, text="C",padx=15,pady=10,command=clear).grid(row=0,column=3,padx=(8,0),pady=5)
Button(root, text="=",padx=20,pady=10,command=evaluate).grid(row=4,column=2, padx=5, pady=5)

root.mainloop()