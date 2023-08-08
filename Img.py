# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter import PhotoImage
from MyLabel import MyLabel

"""Img element"""


class Img(MyLabel):
    def __init__(self, master, image_path):
        self.image = PhotoImage(file=image_path)
        super().__init__(master, image=self.image)
