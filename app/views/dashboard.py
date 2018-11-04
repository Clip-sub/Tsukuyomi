from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def initialize():
    # Do some stuff
    return render_template('../templates/dashboard.html')