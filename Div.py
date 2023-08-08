from Html import Html
from MyFrame import MyFrame

"""Div = Additional element needed to achieve a desired layout."""


class Div(MyFrame, Html):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
