from flask import Blueprint, render_template
from .models import Club, Player, Tournament

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/clubs')
def clubs():
    clubs = Club.query.all()
    return render_template('clubs.html', clubs=clubs)

@bp.route('/players')
def players():
    players = Player.query.filter_by(looking_for_roster=True).all()
    return render_template('players.html', players=players)

@bp.route('/tournaments')
def tournaments():
    tournaments = Tournament.query.order_by(Tournament.date).all()
    return render_template('tournaments.html', tournaments=tournaments)
