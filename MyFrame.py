from tkinter import Frame
from InheritMixin import InheritMixin


class MyFrame(InheritMixin, Frame):
    def __init__(self, master, *args, **kwargs):
        # Get the background color from the master widget
        super().__init__(master, *args, **kwargs)
