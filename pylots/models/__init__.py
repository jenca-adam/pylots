from jinja2 import Environment,BaseLoader
from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import declarative_base,sessionmaker
from ..html.elements import *
from ..html.elements import _element
import json
engine=create_engine('sqlite:///main.db')
Base = declarative_base()
Session=sessionmaker(bind=engine)
session=Session()
def _query(a,b):
    if b not in a:
        return {}
    return a[b]
def by_name(name):
    try:
        return session.query(_model).filter(_model.name==name)[0]
    except IndexError:
        return None
class _model(Base):
    __tablename__='models'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    code=Column(String)
Base.metadata.create_all(engine)
class Model():
    def __init__(self,name,**kwargs):
        self.name=name
        self.kwargs=kwargs
        self.columns=[]
    def register(self,element):
        self.columns.append(repr(element))
        model=by_name(self.name)
        if model is None:
            model=_model(name=self.name,code=json.dumps(self.columns))

            session.add(model)
            session.commit()
        model.code=json.dumps(self.columns)
        session.commit()

    def render(self,dct):
        final=""
        for i in self.columns:
            m=eval(i)
            final+=m.as_html()+'\n'
        env=Environment(loader=BaseLoader)
        m=env.from_string(final).render(dct)
        return m

