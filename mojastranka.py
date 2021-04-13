from pylots.models import Model
from pylots.html.elements import *
from pylots.fields import Field

m=Model('mojmodel')
h=Body('')
a=Div('',class_='w3-container')
h.add_subelem(a)
a.add_subelem(Div(Field('div')))
m.register(h)
print(m.render({'div':'text'}))

