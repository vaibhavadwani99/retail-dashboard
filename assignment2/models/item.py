from db import db


class ItemModel(
    db.Model
):  # this tells sqlalchemy that these are the objects sqlalchemy should interact with
    # now we need to tell sqlalchemy about the data base
    __tablename__ = "items"
    pid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    # name = db.Column(db.String(80))
    sale_amount = db.Column(db.String(80))
    # price = db.Column(db.Float(precision=2))
    profit_percentage = db.Column(db.String(80))

    def __init__(self, pid, description, sale_amount, profit_percentage):
        self.pid = pid
        self.description = description
        self.sale_amount = sale_amount
        self.profit_percentage = profit_percentage

    def json(self):
        return {
            "pid": self.pid,
            "description": self.description,
            "sale_amount": self.sale_amount,
            "profit_percentage": self.profit_percentage,
        }

    @classmethod
    def find_by_pid(cls, pid):
        # sqlalchemy returning row as an object
        return cls.query.filter_by(pid=pid).first()

    def save_to_db(self):

        db.session.add(self)  # sqlalchemy adding object as a row
        db.session.commit()  # session is a collection of objects we can write to the database

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
