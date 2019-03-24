from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
   return render_template('form.html')

@app.route('/record',methods = ['POST'])
def record():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
