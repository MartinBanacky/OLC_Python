from tkinter import Label, PhotoImage


class Img(Label):
    def __init__(self, master, image_path):
        bg_color = master.cget('background')
        self.image = PhotoImage(file=image_path)
        super().__init__(master, image=self.image,bg = bg_color)
