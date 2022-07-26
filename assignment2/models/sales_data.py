from db import db


class Sales_data_model(db.Model):

    __tablename__ = "sales_data"
    sid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    sale_amount = db.Column(db.Integer)
    sale_date = db.Column(db.String(80))

    def __init__(self, user_id, product_id, sale_amount, sale_date):

        self.user_id = user_id
        self.product_id = product_id
        self.sale_amount = sale_amount
        self.sale_date = sale_date

    def json(self):
        return {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "sale_amount": self.sale_amount,
            "sale_date": self.sale_date,
        }

    @classmethod
    def find_by_sid(cls, sid):
        # sqlalchemy returning row as an object
        return cls.query.filter_by(sid=sid).first()

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(sale_date=date).all()

    def save_to_db(self):

        db.session.add(self)  # sqlalchemy adding object as a row
        db.session.commit()  # session is a collection of objects we can write to the database

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
