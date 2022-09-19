from flask_restful import Resource, reqparse
from models.user import UserModel


# allowing users to sign up


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="this field cannot be blank"
    )
    parser.add_argument(
        "password", type=str, required=True, help="this field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username already exist"}, 400
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user is created successfully"}, 201
