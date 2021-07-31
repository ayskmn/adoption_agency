from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png'

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)	   
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)




