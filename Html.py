from tkinter import Tk


class Html(Tk):
    def __init__(self, res):

        super().__init__()
        self.geometry(res)

        self.child_widgets = []

    def add_child(self, widget):
        # Add the child widget to the list
        self.child_widgets.append(widget)

    def pack_all_children(self):
        # Call pack() on all child widgets
        for widget in self.child_widgets:
            widget.pack(expand=True)
            # widget.pack(anchor='w')

    def reset_all_children(self, widget):
        if hasattr(widget, 'reset_to_default'):
            widget.reset_to_default()
        else:
            for child in widget.winfo_children():
                self.reset_all_children(child)

    def on_button_click(self, event):
        print("Person info:")
        for child in self.child_widgets:
            self.reset_all_children(child)


# self.master.event_generate("<Button-1>", x=event.x, y=event.y)  - ak klikneme na vlozit tak nam vypise aj cislo formulara
