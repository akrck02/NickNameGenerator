from PIL import Image, ImageTk
from functools import partial

import tkinter 
import customtkinter 
import Constant
import Generator

# Create the window
def create():

    # appearance settings
    customtkinter.set_appearance_mode(Constant.THEME)  
    customtkinter.set_default_color_theme(Constant.COLOR_THEME) 

    # declare the window
    window = customtkinter.CTk()  
    window.title(Constant.WINDOW_TITLE)
    window.configure(
        width = Constant.WINDOW_WIDTH, 
        height = Constant.WINDOW_HEIGHT
    )
    
    window.geometry('{width}x{height}'.format(width = Constant.WINDOW_WIDTH, height = Constant.WINDOW_HEIGHT))

    # Create the label
    label = customtkinter.CTkLabel(window)
    label.configure(
        text = Constant.LABEL_CLICK_TEXT,
        font = Constant.WINDOW_FONT,
        pady = 100
    )
    label.pack()

    # Create a Button with an icon
    icon_size = Constant.BUTTON_ICON_SIZE
    button_icon = ImageTk.PhotoImage(Image.open(Constant.BUTTON_ICON_PATH).resize((icon_size, icon_size)))

    button = customtkinter.CTkButton (
        master = window, 
        text = Constant.BUTTON_TEXT, 
        image = button_icon, 
        command = partial(Generator.name, label), 
        compound = Constant.RIGHT_ALIGN
    )

    button.place (
        relx = 0.5, 
        rely = 0.65, 
        anchor = tkinter.CENTER
    )

    return window;