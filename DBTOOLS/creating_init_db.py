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
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Cat {self.name}>'
    
class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

class Favourite(Base):
    __tablename__ = 'favourite'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cat_id = db.Column(db.String, db.ForeignKey('cat.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Favourite {self.id}>'


# Configure SQLite database
engine = create_engine('sqlite:///database.db', echo=True)

# Create all tables
Base.metadata.create_all(engine)
