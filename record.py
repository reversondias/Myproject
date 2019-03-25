from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ConfigParser
 
from schemadb import Myproject, Base

class Record:
  def __init__(self,path):
	
	self.config = ConfigParser.ConfigParser()
        self.config.read(path)

  def record_db(self,dict_form):

	config_server = dict(self.config.items('server'))

	engine = create_engine('mysql://'+config_server['user']+':'+config_server['passwd']+config_server['server']+'/'+config_server['db'])
	Base.metadata.bind = engine
 
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
 
	new_pet = Myproject(name=dict_form['name'],color=dict_form['color'],pet=dict_form['pet'])
	session.add(new_pet)
	session.commit()

  def find_duplicate_name(self,name):
	config_server = dict(self.config.items('server'))
	engine = create_engine('mysql://'+config_server['user']+':'+config_server['passwd']+config_server['server']+'/'+config_server['db'])
	Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

	result = session.query(Myproject).filter(Myproject.name == name).first()
	if result:
		return 1
	else:
		return 0
