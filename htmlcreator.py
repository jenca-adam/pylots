from pylots.html.elements import *
Html=HTMLElement('html','Html')
H1=HTMLElement('h1','H1')


zaklad=Html('')
hlavicka=Head('')
hlavicka.add_subelem(Title('Tu je titulok!'))
telo=Body('Nejaky text',[],'right')
zaklad.add_subelem(hlavicka)
zaklad.add_subelem(telo)
telo.add_subelem(H1('Tu je titulok!'))


final=zaklad.as_html()
