from flask import Blueprint, render_template 
from simpledu.models import Live
live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    live = Live.query.order_by("-id").first()
    return render_template('live/index.html',live=live)

