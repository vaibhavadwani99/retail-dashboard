from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "pid",
        type=int,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "description",
        type=str,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "sale_amount",
        type=str,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "profit_percentage",
        type=str,
        required=True,
        help="this field cannot be left blank",
    )

    @jwt_required()
    def get(self, pid):

        item = ItemModel.find_by_pid(pid)
        if item:
            return item.json()
        return {"message": "item not found"}, 404

    @jwt_required()
    def post(self, pid):  # creating the item you want
        if ItemModel.find_by_pid(pid):
            return {"message": "an item with {} already exist".format(pid)}, 400

        request_data = Item.parser.parse_args()
        item = ItemModel(
            request_data["pid"],
            request_data["description"],
            request_data["sale_amount"],
            request_data["profit_percentage"],
        )

        try:
            item.save_to_db()
        except:
            return {
                "message": "An error occured while inserting the item"
            }, 500  # internal server error

        return item.json(), 201

    @jwt_required()
    def delete(self, pid):

        item = ItemModel.find_by_pid(pid)
        if item:
            item.delete_from_db()
        return {"message": "item deleted"}

    @jwt_required()
    def put(self, pid):
        request_data = Item.parser.parse_args()

        item = ItemModel.find_by_pid(pid)

        if item is None:
            item = ItemModel(
                request_data["pid"],
                request_data["description"],
                request_data["sale_amount"],
                request_data["profit_percentage"],
            )
        else:

            item.description = request_data["description"]
            item.sale_amount = request_data["sale_amount"]
            item.profit_percentage = request_data["profit_percentage"]
        item.save_to_db()

        return item.json()


class item_list(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
