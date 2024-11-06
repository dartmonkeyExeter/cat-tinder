from app.extensions import db

class Cat(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(64), index=True)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    uploaded = db.Column(db.DateTime, index=True)
    breed = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'<Cat {self.name}>'