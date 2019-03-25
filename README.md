Myproject
=========
It's a simple python application that save the name, favorite color and pet (dog or cat) in a database.

Requirements
------------
The application require the follow python modules:  

Flask  
MySQL-python  
SQLAlchemy  
gunicorn  
configparser  

On repository there is a requirements.txt. Can you use that to resolve the requriments.
You can use the command:  
#sudo pip install -r requirements.txt  

Configuration Data Base
-----------------------
For data base configuration you must use the conf/db.conf file to set the parameters:  

"db" is the database name  
"user" is the user can permission acess to database  
"passwd" the user password  
"server" the data base server  

Exemple:  

[server]  
db=database_name  
user=user  
passwd=password  
server=localhost  

Description
-----------
The application use flask microframework to make a web application.
To comunicate to database it use SQLAlchemy and the data base is MariaDB. An use Gunicorn with a application server WSGI.  

Its divided in:  

conf  
&nbsp;&nbsp;db.conf   -> Configuration data base parameters  
templates  
&nbsp;&nbsp;form.html -> HTML Fomulary  
index.py    -> The main file to run flask application  
record.py   -> The persist class. Comunicate with the database  
schemadb.py -> The table schema  
wsgi.py     -> To start web application  

To run the application on the home directory run the follow command:  
#sudo gunicorn --bind 0.0.0.0 wsgi  

The default port is 8000. If you want to change, use "0.0.0.0:8080".  
In this case, the application liten to every IP address.  
