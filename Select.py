from tkinter import StringVar
from tkinter.ttk import Combobox


class Select(Combobox):
    def __init__(self, master, options):
        super().__init__(master, values=options)