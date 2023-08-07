from tkinter import Entry


class Input(Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Additional initialization for the Input widget, if needed


# class InputElement:
#     def __init__(self, master):
#         self.master = master

#         self.input_text = StringVar()

#         self = Entry(self.master, textvariable=self.input_text)

#     # def create_input(self):
#     #     self.input_entry = tk.Entry(self.master, textvariable=self.input_text)
#     #     self.input_entry.pack()

#     #     self.master.after(20, self.set_input_width)

#     # def set_input_width(self):
#     #     new_width = self.master.winfo_width()/40
#     #     self.input_entry.config(width= int(new_width))
