class ToDos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))
    completed = db.Column(db.Boolean, default=False)

db.create_all()
sample_todo = ToDos(
    task = "Sample todo",
    completed = False
)
db.session.add(sample_todo)
db.session.commit()