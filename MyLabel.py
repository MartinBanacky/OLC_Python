from tkinter import Label
from InheritMixin import InheritMixin


class MyLabel(InheritMixin, Label):
    def __init__(self, master, *args, **kwargs):
        # Get the background color from the master widget
        super().__init__(master, *args, **kwargs)

        