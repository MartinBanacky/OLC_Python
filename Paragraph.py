from MyLabel import MyLabel

class Paragraph(MyLabel):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, justify='left')