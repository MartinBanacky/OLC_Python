# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter import Label
from InheritMixin import InheritMixin

"""Label with mixin"""


class MyLabel(InheritMixin, Label):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
