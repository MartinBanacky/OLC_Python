# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

"""InheritMixin"""

class InheritMixin:
    def __init__(self, master, *args, **kwargs):
        # Get the background color from the master widget
        bg_color = master.cget('background')
        kwargs['bg'] = bg_color  # Set the background color

        self.child_widgets = []
        super().__init__(master, *args, **kwargs)

    """Func to add child into child_widgets array"""

    def add_child(self, widget):
        # Add the child widget to the list
        self.child_widgets.append(widget)

    """Function call pack() on all child widgets"""

    def pack_all_children(self):
        for widget in self.child_widgets:
            widget.pack(expand=True)  # centered
            # widget.pack(anchor='w') #top left corner as html
