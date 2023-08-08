# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from tkinter.ttk import Combobox

"""Paragraph element"""


class Select(Combobox):
    def __init__(self, master, options):
        super().__init__(master, values=options)

    """Function to print inserted value (Undefined if blank) and sets value to default"""

    def reset_to_default(self):
        chosen_value = self.get()
        if (chosen_value == ""):
            print("Undefined")
        else:
            print(chosen_value)
            self.set('')
