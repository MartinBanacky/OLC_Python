

class InheritMixin:
    def __init__(self, master, *args, **kwargs):
        # Get the background color from the master widget
        bg_color = master.cget('background')
        kwargs['bg'] = bg_color  # Set the background color explicitly

        self.child_widgets = []
        super().__init__(master, *args, **kwargs)

    def add_child(self, widget):
        # Add the child widget to the list
        self.child_widgets.append(widget)

    def pack_all_children(self):
        # Call pack() on all child widgets
        for widget in self.child_widgets:
            widget.pack(expand=True)
            # widget.pack(anchor='w')
