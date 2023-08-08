from tkinter import Button


class PrintButton(Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

        self.bind("<Button-1>", self.buttonClickedEvent)

    def buttonClickedEvent(self, event):
        self.event_generate("<<ClickEvent>>", x=event.x, y=event.y)
