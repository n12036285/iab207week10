from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    # Query the databse for all destinations 
    destinations = db.session.scalars(db.select(Destination)).all()    
    # Renders and sends list of destinations to index.html 
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    # checks if the field exists and not empty 
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        #
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))





