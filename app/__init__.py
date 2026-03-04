from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .discord_models import init_db as init_discord_db

db = SQLAlchemy()
discord_db_session = None

def create_app():
    global discord_db_session
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    db.init_app(app)
    discord_db_session = init_discord_db('sqlite:///discord-bot/discord_bot.db')

    from . import views
    app.register_blueprint(views.bp)

    return app
