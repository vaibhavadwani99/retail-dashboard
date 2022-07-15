from db import db


class Unique_visitors_model(db.Model):

    __tablename__ = "unique_visitors"
    name = db.Column(db.String(80), primary_key=True)
    value = db.Column(db.Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def json(self):
        return {"unique_visitors": self.value}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
