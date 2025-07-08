import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Buttons")
window.geometry("400x300")

def button_func():
    print("Button is clicked")
    button_label = tkinter.Label(window, text="Button was clicked!", font=('Arial', 14))
    button_label.pack(pady=3)

button = ttk.Button(window)
button_string = tkinter.StringVar(value = "Click Me")
button.config(command=button_func, textvariable=button_string)
button.pack(pady=3)

# checkbox

check = ttk.Checkbutton(master = window)
check_var = tkinter.BooleanVar(value=False)
check.config(text = "Check Button", command = lambda: print(check_var.get()), variable=check_var,
             onvalue= True, offvalue=False)
print(check_var.get())
check.pack(pady=3)

# radio buttons

radio_var = tkinter.StringVar(value = "Option 1")
radio1 = ttk.Radiobutton(master=window, text="Option 1", variable=radio_var, value="Option 1", command = lambda : print("Radio 1 is pressed"))
radio2 = ttk.Radiobutton(master=window, text="Option 2", variable=radio_var, value="Option 2")
radio3 = ttk.Radiobutton(master=window, text="Option 3", variable=radio_var, value="Option 3")
radio1.pack(pady=3)
radio2.pack(pady=3)
radio3.pack(pady=3)

window.mainloop()
