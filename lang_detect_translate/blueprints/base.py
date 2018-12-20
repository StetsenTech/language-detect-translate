"""Base blueprint for the application"""
from flask import Blueprint, current_app, render_template, request, url_for

bp = Blueprint('base_route',__name__)

@bp.route("/")
def index():
    """Base route for single page application"""
    return render_template('index.html')

@bp.route('/status')
def status():
    """Indicates that the API is working and returns all routes"""
    for rule in current_app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = "{:35s} {:20s} {}".format(rule.endpoint, methods, url)
        print line
    
    return 'API is up and running!'
    