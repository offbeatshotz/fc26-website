from app import create_app, db
from app.models import Club, Player, Tournament
from datetime import datetime

app = create_app()
with app.app_context():
    # Clear existing data (optional, for fresh runs)
    db.drop_all()
    db.create_all()

    # Add dummy Clubs
    club1 = Club(name="Elite Gamers", description="A club for competitive players.")
    club2 = Club(name="Casual Crew", description="Just having fun with games.")
    club3 = Club(name="Pro Players Guild", description="Dedicated to esports.")

    db.session.add_all([club1, club2, club3])
    db.session.commit()

    # Add dummy Players
    player1 = Player(username="GamerX", gamertag="GamerX#1234", looking_for_roster=True)
    player2 = Player(username="NoobMaster", gamertag="NoobMaster#5678", looking_for_roster=False)
    player3 = Player(username="ProKiller", gamertag="ProKiller#9999", looking_for_roster=True)

    db.session.add_all([player1, player2, player3])
    db.session.commit()

    # Add dummy Tournaments
    tournament1 = Tournament(name="Weekly Brawl", date=datetime(2026, 3, 10, 19, 0, 0), description="A weekly tournament for all players.")
    tournament2 = Tournament(name="Spring Championship", date=datetime(2026, 4, 15, 14, 0, 0), description="Big prize pool!")

    db.session.add_all([tournament1, tournament2])
    db.session.commit()

    print("Dummy data added to the database!")
