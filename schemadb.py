from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Myproject(Base):
    __tablename__ = 'pet_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    color = Column(String(250), nullable=False)
    pet = Column(String(4), nullable=False)
