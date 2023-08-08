# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter import Entry

"""Input element"""


class Input(Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

    """Function to print inserted value (Undefined if blank) and sets value to default"""

    def reset_to_default(self):
        text_input = self.get()
        if (text_input == ""):
            print("Undefined")
        else:
            print(text_input)
            self.delete(0, 'end')
