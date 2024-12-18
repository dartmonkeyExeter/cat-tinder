from app.extensions import db

class Cat(db.Model):
    id = db.Column(db.String, primary_key=True)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Cat {self.name}>'