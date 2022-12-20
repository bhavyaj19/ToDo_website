from flask import Blueprint, render_template

site='website/templates\index.html'
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('index.html')