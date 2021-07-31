from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_all_pets():
	pets = Pet.query.all()
	return render_template('homepage.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
	"""Add new pet."""

	form = AddPetForm()

	if form.validate_on_submit():
		data = {k: v for k, v in form.data.items() if k != "csrf_token"}
		new_pet = Pet(**data)

		db.session.add(new_pet)
		db.session.commit()
		flash(f"{new_pet.name} added!", "success")
		return redirect('/')
	
	else:
		return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
	"""Get the form data and redirect to homepage"""
	pet = Pet.query.get_or_404(pet_id)
	form = EditPetForm(obj=pet)

	if form.validate_on_submit():
		pet.notes= form.notes.data
		pet.available= form.available.data
		pet.photo_url= form.photo_url.data
		db.session.commit()
		flash(f"{pet.name} updated", "success")
		return redirect('/')
	else:
		return render_template("edit_pet_form.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
   	"""Return basic info about pet in JSON."""

   	pet = Pet.query.get_or_404(pet_id)
   	info = {"name": pet.name, "age": pet.age}

   	return jsonify(info)