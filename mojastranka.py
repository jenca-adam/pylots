from pylots.models import Model
from pylots.html.objects import *
class MojModel(Model):
    moje_pole=Paragraph(class_='w3-jumbo',id='bordered')
    moje_dalsie_pole=Paragraph(class_='w3-tiny',id='paragraf2',argumentik='hodnoticka')
m=MojModel(moje_pole={'text':'Tu je nejaky nahodny text'},moje_dalsie_pole={'text':'Tu je druhy paragraf'})
print(m.as_html())
