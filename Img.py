from tkinter import Label, PhotoImage


class Img(Label):
    def __init__(self, master, image_path):
        self.image = PhotoImage(file=image_path)
        super().__init__(master, image=self.image)
