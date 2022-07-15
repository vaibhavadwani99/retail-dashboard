from flask_restful import Resource, reqparse
from models.total_sales import Total_sales_model


class Total_sales(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "name", type=str, required=True, help="this field cannot be blank"
    )
    parser.add_argument(
        "value", type=str, required=True, help="this field cannot be blank"
    )

    def get(self, name):
        total_sales = Total_sales_model.find_by_name(name)
        if total_sales:
            return total_sales.json()
        else:
            return {"message": "total sales not found"}

    def put(self, name):
        data = Total_sales.parser.parse_args()

        item = Total_sales_model.find_by_name(name)

        if item is None:
            item = Total_sales_model(data["name"], data["value"])
        else:
            item.value = data["value"]
            item.name = data["name"]
        item.save_to_db()

        return item.json()
