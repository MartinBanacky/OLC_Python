from tkinter import Frame

"""Div = Additional element needed to achieve a desired layout."""
class Div(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
