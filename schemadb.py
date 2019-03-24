from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Myproject(Base):
    __tablename__ = 'myproject'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    color = Column(String(250), nullable=False)
    animal = Column(String(250), nullable=False)
 

engine = create_engine('mysql://user_project:projectdb2019@localhost/project')
 
Base.metadata.create_all(engine)
