from flask import Flask, render_template, request
from record import Record
application = Flask(__name__)

path_db_conf="conf/db.conf"

@application.route('/', methods=['POST','GET'])
def form():
   if request.method == 'POST':
      result_form = request.form

      record = Record(path_db_conf)
      result_name = record.find_duplicate_name(result_form['name'])
      if result_name == 0:
          result_db = record.record_db(result_form)
          return render_template("form.html",result = "Success to save!")
      else:
          return render_template("form.html",result = "There is this name!")
   else:
     return render_template('form.html')

