from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/dojo/new',methods=['POST'])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    print(data)
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show(id):
    print(id)
    data ={ 
        "id":id
    }
    return render_template("show_ninjas.html",dojo=Dojo.get_ninjas_with_dojo(data))