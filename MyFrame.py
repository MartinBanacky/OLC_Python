# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter import Frame
from InheritMixin import InheritMixin

"""Frame with mixin"""


class MyFrame(InheritMixin, Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
