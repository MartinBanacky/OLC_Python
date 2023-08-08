from tkinter.ttk import Combobox


class Select(Combobox):
    def __init__(self, master, options):
        super().__init__(master, values=options)

    def reset_to_default(self):
        chosen_value = self.get()
        print(chosen_value)
        self.set('')
