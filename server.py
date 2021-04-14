from pylots.app import App
from pylots.html.elements import *
from htmlcreator import final
m=App()
@m.path('/')
def p(request):
   return final
@m.path('/wre/')
def wre(request):
    return open('wre.html').read()
m.run(5000)
