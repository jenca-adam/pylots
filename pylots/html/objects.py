from jinja2 import Environment,BaseLoader

class HTMLObject:
    def __init__(self,string):
        self.string=string
    def as_html(self,data):
         _template=Environment(loader=BaseLoader).from_string(self.string)
         return _template.render(**data)
    def __repr__(self):
        repre=self.__name__+"("
        for i in self.kwargs:
            repre+=i+"="+'"'+self.kwargs[i]+'",'

        repre+=")"
        return repre
        
class Paragraph(HTMLObject):
    def __init__(self,**kwargs):
        self.__name__='Paragraph'
        string="<p"
        self.kwargs=kwargs
        for i in kwargs:
            string+=' '+i.replace('_','')+'= "'+kwargs[i]+'"'
        string+='>{{text}}</p>'
        super().__init__(string)


