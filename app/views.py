from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Vehicle
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    # Query all vehicles from the database
    vehicles = Vehicle.query.all()

    return render_template("home.html", user=current_user, vehicles=vehicles)

@views.route('/add_vehicle', methods=['GET', 'POST'])
@login_required
def add_vehicle():
    if request.method == 'POST':
        # Extract form data
        make = request.form['make']
        model = request.form['model']
        year = int(request.form['year'])
        vin = request.form['vin']
        odometer = int(request.form['odometer'])
        color = request.form['color']
        owner_name = request.form['owner_name']

        # Create a new Vehicle instance
        new_car = Vehicle(
            make=make,
            model=model,
            year=year,
            vin=vin,
            odometer=odometer,
            color=color,
            owner_name=owner_name
        )

        # Add the new car to the database
        db.session.add(new_car)
        db.session.commit()

        return redirect(url_for('views.home'))

    return render_template('add_vehicle.html', user=current_user)