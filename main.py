from Div import Div
from Anchor import Anchor
from Form import Form
from Img import Img
from Input import Input
from Paragraph import Paragraph
from Select import Select
from Html import Html



html = Html("1280x720")

div_body = Div(html, bg = "lightgrey")

div_body_header = Div(div_body, highlightbackground="black", highlightthickness=2)
p_header = Paragraph(div_body_header, "Please fill information below:")

form = Form(div_body)

div_name = Div(div_body)
p_name = Paragraph(div_name, "Name:")
input_name = Input(div_name)

select = Select(form, ["Muz", "Zena"])
hyperlink = Anchor(form, text="google it!", url="https://www.google.com/")
img = Img(div_body_header, "photo.png")

html.add_child(div_body)
html.add_child(div_body_header)
html.add_child(p_header)
html.add_child(img)
html.add_child(div_name)
html.add_child(p_name)
html.add_child(input_name)
html.add_child(form)
html.add_child(select)
html.add_child(hyperlink)


html.pack_all_children()


html.mainloop()
