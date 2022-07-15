from db import db


class Average_sales_model(db.Model):

    __tablename__ = "average_Sales"
    name = db.Column(db.String(80), primary_key=True)
    value = db.Column(db.String(80))

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def json(self):
        return {"average_sales": self.value}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()