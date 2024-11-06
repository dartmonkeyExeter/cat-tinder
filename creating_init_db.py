from app.extensions import db
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Assuming db is already initialized in `app.extensions`
Base = declarative_base()

# Define the Cat model
class Cat(Base):
    __tablename__ = 'cat'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(64), index=True)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    uploaded = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    breed = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'<Cat {self.name}>'

# Configure SQLite database
engine = create_engine('sqlite:///database.db', echo=True)

# Create all tables
Base.metadata.create_all(engine)
