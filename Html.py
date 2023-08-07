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
            widget.pack( expand = True)
            #widget.pack(anchor='w')


#self.master.event_generate("<Button-1>", x=event.x, y=event.y)  - ak klikneme na vlozit tak nam vypise aj cislo formulara
