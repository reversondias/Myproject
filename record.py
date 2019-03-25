from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from schemadb import Myproject, Base

class Record:
  def record_db(self,dict_form):

	engine = create_engine('mysql://root@localhost/myproject')
	Base.metadata.bind = engine
 
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
 
	new_pet = Myproject(name=dict_form['name'],color=dict_form['color'],pet=dict_form['pet'])
	session.add(new_pet)
	session.commit()

  def find_duplicate_name(self,name):
	engine = create_engine('mysql://root@localhost/myproject')
        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

	result = session.query(Myproject).filter(Myproject.name == name).first()
	if result:
		return 1
	else:
		return 0
