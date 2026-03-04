from flask import Blueprint, render_template
from .models import Club, Player
from .discord_models import Script
from .__init__ import discord_db_session

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/clubs')
def clubs():
    clubs = Club.query.all()
    recent_scripts = discord_db_session.query(Script).order_by(Script.uploaded_at.desc()).limit(5).all()
    return render_template('clubs.html', clubs=clubs, recent_scripts=recent_scripts)

@bp.route('/players')
def players():
    players = Player.query.filter_by(looking_for_roster=True).all()
    recent_scripts = discord_db_session.query(Script).order_by(Script.uploaded_at.desc()).limit(5).all()
    return render_template('players.html', players=players, recent_scripts=recent_scripts)
