from db import db


class UserModel(db.Model):
    # we need to add information about the table for sqlalchemy
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):

        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(
            id=_id
        ).first()  # cls.query is the query builder present inside db.Model

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
