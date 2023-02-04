from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    note = Note.query.all()
    return render_template("home.html", user=current_user , note=note)

@views.route('/new', methods=["POST"])
@login_required
def add_note():
    if request.method == 'POST':

        # receive data from the form
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        lugar = request.form['lugar']
        direccion = request.form['direccion']
        inicio = request.form['inicio']
        fin = request.form['fin']
        modalidad = request.form['modalidad']

        # create a new note object
        new_note = Note(nombre, categoria, lugar, direccion, inicio, fin, modalidad, user_id = current_user.id)

        # save the object into the database
        db.session.add(new_note)
        db.session.commit()

        flash('Event added successfully!')

        return redirect(url_for('views.home'))

@views.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    # get contact by Id
    print(id)
    note = Note.query.get(id)

    if request.method == "POST":
        note.nombre = request.form['nombre']
        note.categoria = request.form['categoria']
        note.lugar = request.form['lugar']
        note.direccion = request.form['direccion']
        note.inicio = request.form['inicio']
        note.fin = request.form['fin']
        note.modalidad = request.form['modalidad']


        db.session.commit()

        flash('Event updated successfully!')

        return redirect(url_for('views.home'))

    return render_template('update.html', user = current_user, note=note)

@views.route("/delete/<id>", methods=["GET"])
@login_required
def delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    flash('Event deleted successfully!')

    return redirect(url_for('views.home'))
