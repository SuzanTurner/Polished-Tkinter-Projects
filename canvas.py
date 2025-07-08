import tkinter
# from tkinter import ttk
import  ttkbootstrap as ttk  # Import ttkbootstrap for themed widgets

# window = tkinter.Tk()
window = ttk.Window(themename="cosmo")  # Use ttkbootstrap for themed widgets
window.title("Tkiter Paint")
window.geometry("400x400")

x_button = ttk.Button(window, text="X", command=window.quit, width=3, style='danger')
x_button.pack(side='top', anchor='ne', padx=5, pady=5)

label = ttk.Label(window, text='Canvas', font=('Helvetica', 12), border=2, relief='groove', padding=10, foreground='black', background="lightgreen")
label.pack(pady=10)

# Canvas

canvas = tkinter.Canvas(master = window, width=300, height=200, bg='white', border=2, relief='groove')
canvas.pack(pady = 5)


# entry_var = tkinter.StringVar(value = "Type anything")

# entry = tkinter.Entry(window, width=20, textvariable=entry_var, font=('Arial', 14))
# entry.pack(pady=5)

# canvas.create_rectangle(50, 50, 250, 150, fill='yellow', outline='black', width=2)
# canvas.create_oval(100, 75, 200, 125, fill='red', outline='black', width=2)
# canvas.create_line(50, 50, 250, 150, fill='green', width=2)
# canvas.create_text(150, 180, text = "We can create text", font=('Arial', 16), fill='black')

# # dynamic text

# text_label = tkinter.Label(canvas, textvariable=entry_var, font=('Arial', 14), bg = "lightblue")
# text_label.place(x=150, y=10, anchor='n')  # Place the label at the top center of the canvas

brush_size = 2

# def brush_size_adjust(event):
#     global brush_size
#     if event.delta > 0:  # Scroll up
#         brush_size += 1
#     elif event.delta < 0:  # Scroll down
#         brush_size = max(0,min(brush_size, 50)) 
        

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:  # Scroll up
        brush_size = min(brush_size + 1, 50)
    elif event.delta < 0:  # Scroll down
        brush_size = max(1, brush_size - 1)
    print(f"Brush size: {brush_size}")
 # Ensure brush size doesn't go below 1

def draw_on_canvas(event):
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill='black', width = brush_size)


canvas.bind("<B1-Motion>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)


clear_button = ttk.Button(window, text="Clear Canvas", command=lambda: canvas.delete("all"))
clear_button.pack(pady=5)


window.bind("<KeyPress-q>", lambda event : window.quit())

window.mainloop()