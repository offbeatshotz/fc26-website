from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import os

Base = declarative_base()

class Script(Base):
    __tablename__ = 'scripts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    platform = Column(String(50), nullable=False)  # e.g., 'Titan Two', 'Cronus Zen', 'Xim Matrix'
    script_content = Column(Text, nullable=False)
    uploaded_by = Column(String(100), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Script {self.name} ({self.platform})>"

# Database setup (to be called from bot.py or a separate script)
def init_db(database_url):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
