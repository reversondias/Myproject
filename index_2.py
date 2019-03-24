from flask import Flask, render_template, request
from record import Record
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def form():
   if request.method == 'POST':
      result_form = request.form

      record = Record()
      result_name = record.find_duplicate_name(result_form['name'])
      if result_name == 0:
          result_db = record.record_db(result_form)
          return render_template("form.html",result = "Success!")
      else:
          return render_template("form.html",result = "There is this name!")
   else:
     return render_template('form.html')

@app.route('/record',methods = ['POST'])
def record():
   if request.method == 'POST':
      result_form = request.form

      record = Record()
      result_name = record.find_duplicate_name(result_form['name'])
      if result_name == 0:
          result_db = record.record_db(result_form)
      else:
	  print "There is this name!"
          return render_template("form.html",result = 1)
      return render_template("ok.html")
      #return render_template("result.html",result = result)
