from jinja2 import Environment,BaseLoader
import json
class _element:
    def __init__(self,name,string,value,subelem=None,text_format='left',**kwargs):
        self._text_format=text_format
        if text_format not in ['left','right']:
            raise ValueError('text_format must be "left" or "right')
        self._prefix=string
        if subelem is None:
            self.subelem=[]
        else:
            self.subelem=subelem
        self._value=value
        self.__name__=name
        st='<'+self._prefix
        self.kwargs=kwargs
        for i in kwargs:
            st+=' '+i.replace('_','')+'= "'+kwargs[i]+'"'
        st+='>'+value+'</'+self._prefix+'>'
        self.string=st
    def _sublm_format(self):
        if self._text_format=='left':
            return self._value+''.join([i.as_html() for i in self.subelem])
        else:
            return ''.join([i.as_html() for i in self.subelem])+self._value

    def setarg(self,arg,value):
        self.kwargs[arg]=value
        self._refresh()
    def add_subelem(self,elem):
        if not isinstance(elem,_element):
            raise TypeError
        self.subelem.append(elem)
        #self._refresh()
    def as_html(self):
        st='<'+self._prefix

        for i in self.kwargs:
            st+=' '+i.replace('_','')+'= "'+self.kwargs[i]+'"'
        st+='>'+self._sublm_format()+'</'+self._prefix+'>'
        return st
    def _refresh(self):
        self.string=self.as_html()
    def __repr__(self):
        repre=self.__name__+"('"+self._value+"',"+json.dumps([repr(i) for i in self.subelem])+",'"+self._text_format+"',"
        for i in self.kwargs:
            repre+=i+"="+'"'+self.kwargs[i]+'",'

        repre+=")"
        return repre
def HTMLElement(string,name):
    class Object(_element):
        def __init__(self,value,subelem=[],text_align='left',**kwargs):
            super().__init__(name,string,value,subelem,text_align,**kwargs)
    return Object



