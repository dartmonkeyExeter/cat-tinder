from app.extensions import db
from datetime import datetime

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cat_id = db.Column(db.String, db.ForeignKey('cat.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Favourite {self.id}>'