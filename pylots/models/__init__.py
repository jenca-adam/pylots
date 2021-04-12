from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import declarative_base,sessionmaker
from ..html.objects import *
import json
engine=create_engine('sqlite:///main.db',echo=True)
Base = declarative_base()
Session=sessionmaker(bind=engine)
session=Session()
def _query(a,b):
    if b not in a:
        return {}
    return a[b]
class _model(Base):
    __tablename__='models'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    code=Column(String)
Base.metadata.create_all(engine)
class Model():
    def __init__(self,**kwargs):
        self.kwargs=kwargs
        self.columns=[]
        for i in dir(self):
            if isinstance(eval('self.'+i),HTMLObject):
                self.columns.append((repr(eval('self.'+i)),i))
        model=_model(name=self.__class__.__name__,code=json.dumps(self.columns)) 
        session.add(model)
        session.commit()

        
    def as_html(self):
        final=""
        for i in self.columns:
            m=eval(i[0])
            final+=m.as_html(self.kwargs[i[1]])+'\n'
        return final

