import tkinter 
# import ttkbootstrap as ttk
from tkinter import ttk

window = tkinter.Tk()
window.title("Window and Widgets")
window.geometry("400x300")  

# tkinter widgets

text_label = tkinter.Label(window)
text_label.config(text = 'This is a text label', font=('Arial', 14))
text_label.pack(pady=3)

text_box = tkinter.Text(window, height =5, width = 20)
text_box.pack(pady=3)

def button_clicked():
    print("Button clicked!")
    text_label.config(text = 'Button was clicked!')
    text_box.insert(tkinter.END, "Button was clicked!\n")

button = tkinter.Button(window, text='Click Me', command = button_clicked)
button.pack(pady=3)

# ttk widgets

label = ttk.Label(master = window, text='This is a ttk label', font=('Arial', 14))
label.pack(pady=3)

separator = ttk.Separator(master = window, orient='horizontal')
separator.pack(fill='x', pady=3) 

# Using stringVar for dynamic text updates
string_var = tkinter.StringVar(value = "Type Anything")

str_label = ttk.Label(master=window, textvariable=string_var, font=('Arial', 14))
str_label.pack(pady=3)

str_entry = ttk.Entry(master=window, textvariable=string_var, width=20)
str_entry.pack(pady=3)

str_content = ttk.Label(master = window, text = "Whatever you typ will be displayed here", font=('Arial', 14))
str_content.pack(pady=3)

exit_button = ttk.Button(master=window, text='Exit', command=window.destroy)
exit_button.pack(pady=3)

window.mainloop()

