from Div import Div
from Anchor import Anchor
from Form import Form
from Img import Img
from Input import Input
from Select import Select
from Html import Html



html = Html("1280x720")

div = Div(html)
form = Form(div, bg="lightblue")
input = Input(form)
select = Select(form, ["Muz", "Zena"])
hyperlink = Anchor(form, text="google it!", url="https://www.google.com/")
img = Img(form, "photo.png")


html.add_child(input)
html.add_child(select)
html.add_child(hyperlink)
html.add_child(img)
html.add_child(div)
html.add_child(form)

html.pack_all_children()


html.mainloop()
