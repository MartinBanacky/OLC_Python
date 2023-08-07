from tkinter import Frame


"""Form = An area that accepts user input."""
class Form(Frame):
    def __init__(self, master, **kwargs):
        bg_color = master.cget('background')
        super().__init__(master, **kwargs,bg = bg_color)