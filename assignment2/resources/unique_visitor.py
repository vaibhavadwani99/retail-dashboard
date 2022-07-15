from flask_restful import Resource, reqparse
from models.unique_visitors import Unique_visitors_model


class Unique_visitors(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "name", type=str, required=True, help="this field cannot be blank"
    )
    parser.add_argument(
        "value", type=str, required=True, help="this field cannot be blank"
    )

    def get(self, name):
        total_sales = Unique_visitors_model.find_by_name(name)
        if total_sales:
            return total_sales.json()
        else:
            return {"message": "unique visitors not found"}

    def put(self, name):
        data = Unique_visitors.parser.parse_args()

        item = Unique_visitors_model.find_by_name(name)

        if item is None:
            item = Unique_visitors_model(data["name"], data["value"])
        else:
            item.value = data["value"]
            item.name = data["name"]
        item.save_to_db()

        return item.json()
