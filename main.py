from Div import Div
from Anchor import Anchor
from Form import Form
from Img import Img
from Input import Input
from Paragraph import Paragraph
from PrintButton import PrintButton
from Select import Select
from Html import Html



html = Html("1280x720")

div_body = Div(html, highlightbackground="grey", highlightthickness=2)

div_body.configure(bg="lightgrey")

div_body_header = Div(div_body, highlightbackground="black", highlightthickness=2)
img = Img(div_body, "photo.png")
p_header = Paragraph(div_body_header, "Please fill information below:")

form_info = Form(div_body)

div_name = Div(form_info)
#div_name.configure(bg="red")
p_name = Paragraph(div_name, "Name:")
input_name = Input(div_name)

p_gender = Paragraph(form_info, "Choose gender:")
select_gender = Select(form_info, ["Man", "Woman"])

div_age = Div(form_info)
p_age = Paragraph(div_age, "Age:")
input_age = Input(div_age)

div_height = Div(form_info)
p_height = Paragraph(div_height, "Height:")
input_height = Input(div_height)

print_button = PrintButton(div_body,"Submit")

hyperlink = Anchor(div_body, text="Look me up on LinkedIn", url="https://www.linkedin.com/in/martinbanacky/")

html.bind("<<ClickEvent>>", html.on_button_click)

html.add_child(div_body)


div_body.add_child(div_body_header)
div_body_header.add_child(img)
div_body_header.add_child(p_header)

div_body.add_child(form_info)

form_info.add_child(div_name)
div_name.add_child(p_name)
div_name.add_child(input_name)

form_info.add_child(p_gender)
form_info.add_child(select_gender)

form_info.add_child(div_age)
div_age.add_child(p_age)
div_age.add_child(input_age)

form_info.add_child(div_height)
div_height.add_child(p_height)
div_height.add_child(input_height)

div_body.add_child(print_button)

div_body.add_child(hyperlink)

html.pack_all_children()
div_body_header.pack_all_children()
div_body.pack_all_children()
form_info.pack_all_children()
div_name.pack_all_children()
div_age.pack_all_children()
div_height.pack_all_children()


html.mainloop()
