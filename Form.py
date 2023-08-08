# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from MyFrame import MyFrame


"""Form element = An area that accepts user input."""


class Form(MyFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
