from app import db, models

ds=models.Dataset.query.all()
for d in ds:
    db.session.delete(d)
db.session.commit()
