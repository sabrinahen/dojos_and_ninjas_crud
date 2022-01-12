from flask import render_template, request, redirect

from flask_app import app
# from flask_app.models.ninja import Ninja
from flask_app.models import ninja, dojo
# from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", dojos=dojo.Dojo.get_all())

@app.route('/ninja/new',methods=['POST'])
def create_ninja():
    print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojos_id": request.form["dojo_id"]
    }
    print(data)
    # Ninja.save(request.form)
    ninja.Ninja.save(data)
    return redirect('/ninjas')