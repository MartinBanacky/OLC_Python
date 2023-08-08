# -- Copyright  2023 Martin Baňacký

# -- All rights reserved.

from MyLabel import MyLabel

"""Paragraph element"""


class Paragraph(MyLabel):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, justify='left')
