from tkinter import Label
import webbrowser


class Anchor(Label):
    def __init__(self, master, text, url, *args, **kwargs):
        super().__init__(master, text=text, fg='blue', cursor='hand2', *args, **kwargs)

        self.url = url
        self.bind("<Button-1>", self.open_link)

    def open_link(self, event):
        webbrowser.open(self.url)
