from application import db

class ToDos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))
    completed = db.Column(db.Boolean, default=False)

