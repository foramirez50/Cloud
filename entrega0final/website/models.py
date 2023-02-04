from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(1000))
    categoria = db.Column(db.String(1000))
    lugar = db.Column(db.String(1000))
    direccion = db.Column(db.String(1000))
    inicio = db.Column(db.String(1000))
    fin = db.Column(db.String(1000))
    modalidad = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, nombre, categoria, lugar, direccion, inicio, fin, modalidad, user_id):
        self.nombre = nombre
        self.categoria = categoria
        self.lugar = lugar
        self.direccion = direccion
        self.inicio = inicio
        self.fin = fin
        self.modalidad = modalidad
        self.user_id = user_id

class User(db.Model, UserMixin): 
    #we use usermixin to don't do the login from 0
    id = db.Column(db.Integer, primary_key=True) #put incremental 
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')# list of all the notes that a user has, pute tne name of another class
