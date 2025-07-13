import customtkinter as ctk
from tkinter import ttk
from settings import *

try:
    from ctypes import windll, byref, c_int, sizeof
except Exception as e:
    print("Found this exeption:", e)


class Grip(ttk.Sizegrip):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=3, column=0, sticky="se")

        # A single parent can have only one, either pack() or grid()

class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi):
        font = ctk.CTkFont(family= FONT, size = MAIN_TEXT_SIZE, weight = "bold")
        super().__init__(parent, text= "22.5", font= font, text_color = WHITE, textvariable = bmi)
        self.grid(row = 0, column = 0, rowspan = 2,  sticky = "news")

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, w):
        super().__init__(parent, fg_color= WHITE)
        self.grid(row = 2, column = 0, sticky = "news", padx = 10, pady = 10)
        self.w = w

        self.columnconfigure((0), weight = 2, uniform= "b")
        self.columnconfigure((1), weight = 1, uniform= "b")
        self.columnconfigure((2), weight = 3, uniform= "b")
        self.columnconfigure((3), weight = 1, uniform= "b")
        self.columnconfigure((4), weight = 2, uniform= "b")
        self.rowconfigure((0), weight = 1, uniform= "b")

        self.output_string = ctk.StringVar()

        self.label(self.output_string)
        self.update_weight()
        self.signs()

    def label(self, output_string):
        font = ctk.CTkFont(family= FONT, size = INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, textvariable = output_string, font = font, text_color= BLACK)
        label.grid(row = 0, column = 2)

    def signs(self):
        font = ctk.CTkFont(family= FONT, size = INPUT_FONT_SIZE)
        minus_button = ctk.CTkButton(self, text = "-", 
                                     command = lambda : self.update_weight(('minus', 'large')),
                                     font = font, text_color= BLACK, fg_color= LIGHT_GRAY, hover_color= GRAY)
        minus_button.grid(row = 0, column = 0, sticky = "ns", padx = 8, pady = 8)

        plus_button = ctk.CTkButton(self, text = "+", 
                                    command = lambda : self.update_weight(('plus', 'large')),
                                    font = font, text_color= BLACK, fg_color= LIGHT_GRAY, hover_color= GRAY)
        plus_button.grid(row = 0, column = 4, sticky = "ns", padx = 8, pady = 8)

        small_plus_button = ctk.CTkButton(self, text = "+", 
                                          command = lambda : self.update_weight(('plus', 'small')),
                                          font = font, text_color= BLACK, fg_color= LIGHT_GRAY, hover_color= GRAY)
        small_plus_button.grid(row = 0, column = 3, padx = 4, pady = 4)

        small_minus_button = ctk.CTkButton(self, text = "-", 
                                           command = lambda : self.update_weight(('minus', 'small')),
                                           font = font, text_color= BLACK, fg_color= LIGHT_GRAY, hover_color= GRAY)
        small_minus_button.grid(row = 0, column = 1, padx = 4, pady = 4)

    def update_weight(self, info = None):
        if info:
            amount = 1 if info[1] == 'large' else 0.1
            if info[0] == 'plus':
                self.w.set(self.w.get() + amount)
            else:
                self.w.set(self.w.get() - amount)
        self.output_string.set(f"{round(self.w.get(), 1)}kg")
            

class Slider(ctk.CTkFrame):
    def __init__(self, parent, h):
        super().__init__(parent, fg_color= WHITE)
        self.grid(row = 3, column = 0, sticky = "news", padx = 10, pady = 10)

        self.output_string = ctk.StringVar(value = "hi")
        
        self.slider(h)
        self.output_text(self.output_string)

    def slider(self, h):
        slider = ctk.CTkSlider(self, button_color= GREEN, button_hover_color=DARK_GREEN, variable= h, from_ = 100, to = 250,command = self.update)
        slider.pack(side = "left", expand = True, fill = "x", pady = 10, padx = 10)

    def output_text(self, output_string):
        font = ctk.CTkFont(family= FONT, size = INPUT_FONT_SIZE)
        output_text = ctk.CTkLabel(self, text = "1.80m", text_color= BLACK, font = font, textvariable = output_string)
        output_text.pack(side = "right", padx = 20)

    def update(self, amount):
        # print(amount)
        text = str(int(amount))
        meter = text[0]
        cm = text[1:]
        self.output_string.set(f"{meter}.{cm}m")



class Window(ctk.CTk):
    def __init__(self, title):
        super().__init__(fg_color = GREEN)

        self.title(title)
        self.geometry("400x400")

        self.columnconfigure((0), weight = 1)
        self.rowconfigure((0,1,2,3), weight= 1, uniform= 'a')

        self.height = ctk.IntVar(value = 170)
        self.weight = ctk.DoubleVar(value = 65)
        self.bmi = ctk.StringVar()
        self.update()

        # tracing

        self.height.trace('w', self.update)
        self.weight.trace('w', self.update)

        Grip(self)
        ResultText(self, self.bmi)
        WeightInput(self, self.weight)
        Slider(self, self.height)

        self.change_title_bar_color()
        
        self.bind("<KeyPress-q>", lambda event: self.quit())
        self.mainloop()

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass

    def update(self, *args):
        h = self.height.get() / 100
        w = self.weight.get()
        result = round(w / h ** 2, 2)
        self.bmi.set(result)

if __name__ == "__main__":
    Window("BMI")