import tkinter 
import ttkbootstrap as ttk
# from tkinter import ttk

# window = tkinter.Tk()
window = ttk.Window(themename="superhero")  # Use ttkbootstrap for themed widgets
window.title("Basic GUI")
window.geometry("400x170")

title_label = ttk.Label(window, text = 'Miles to Kilometers Converter', font=('Arial', 16))
title_label.pack(pady=10)

def convert():
    print("convert")
    miles = entry.get()
    try:
        miles = float(miles)
        kilometers = miles * 1.60934
        output_label.config(text=f'Kilometers: {kilometers:.2f}')
    except ValueError:
        output_label.config(text='Please enter a valid number.')

# input

input_frame = ttk.Frame(window)
entry = ttk.Entry(input_frame, width=20)
button = ttk.Button(input_frame, text='Convert', command = convert)
entry.pack(side = 'left',padx = 5,  pady = 5)
button.pack( side = 'left', padx = 5, pady = 5)
input_frame.pack(pady=5)

# output

output_frame = ttk.Frame(window)
output_label = ttk.Label(output_frame, text='Kilometers: ', font = ('Arial', 14))
output_label.pack(pady=5)
output_frame.pack(pady=5)


window.mainloop()

