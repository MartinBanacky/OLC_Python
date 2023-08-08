# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter import Button

"""Button for submit"""


class PrintButton(Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        # bind clicking to call func 'buttonClickedEvent'
        self.bind("<Button-1>", self.buttonClickedEvent)

    # generating event for parent

    def buttonClickedEvent(self, event):
        self.event_generate("<<ClickEvent>>", x=event.x, y=event.y)
