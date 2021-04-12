from pylots.models import Model
from pylots.html.objects import Paragraph
class MyModel(Model):
    field=Paragraph(id="bordered")
    pako=Paragraph(class_="w3-tiny")

model=MyModel(field={'text':"papap"},pako={'text':'mamaaaa'})
print(model.kwargs)
print(model.columns)
print(model.as_html())
