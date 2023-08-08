# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter import Tk

"""Html element"""


class Html(Tk):
    def __init__(self, res):

        super().__init__()
        self.geometry(res)  # res in format "PXxPY"

        self.child_widgets = []  # array for children

    """Func to add child into child_widgets array"""

    def add_child(self, widget):
        # Add the child widget to the list
        self.child_widgets.append(widget)

    """Function call pack() on all child widgets"""

    def pack_all_children(self):
        for widget in self.child_widgets:
            widget.pack(expand=True)  # centered
            # widget.pack(anchor='w') #top left corner as html

    """Recursive Func to reset all child elements"""

    def reset_all_children(self, widget):
        if hasattr(widget, 'reset_to_default'):
            widget.reset_to_default()
        else:
            for child in widget.winfo_children():
                self.reset_all_children(child)

    """Function starts print values and then set them on default"""

    def on_button_click(self, event):
        print("Person info:")
        for child in self.child_widgets:
            self.reset_all_children(child)
