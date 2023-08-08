# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from MyLabel import MyLabel
import webbrowser

"""Anchor element"""


class Anchor(MyLabel):
    def __init__(self, master, text, url, *args, **kwargs):
        super().__init__(master, text=text, fg='blue', cursor='hand2', *args, **kwargs)

        self.url = url
        # bind clicking to call func 'open_link'
        self.bind("<Button-1>", self.open_link)

    # here we open link
    def open_link(self, event):
        webbrowser.open(self.url)
