from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja
# from flask_app.models import ninja

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninja/new',methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    print(data)
    Ninja.save(data)
    # ninja.Ninja.save(data)
    return redirect('/ninjas')