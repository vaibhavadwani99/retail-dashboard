# from datetime import date  # date should be in yyyy-mm-dd format
from flask_restful import reqparse, Resource
from models.sales_data import Sales_data_model


class Sales_data(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "sid",
        type=int,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "user_id",
        type=int,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "product_id",
        type=int,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "sale_amount",
        type=int,
        required=True,
        help="this field cannot be left blank",
    )
    parser.add_argument(
        "date",
        type=str,
        required=True,
        help="this field cannot be left blank",
    )

    def get(self, sid):

        item = Sales_data_model.find_by_sid(sid)
        if item:
            return item.json()
        return {"message": "sale data not found"}, 404

    def post(self, sid):  # creating the item you want

        if Sales_data_model.find_by_sid(sid):
            return {
                "message": "sale data with sale id {} already exist".format(sid)
            }, 400

        request_data = Sales_data.parser.parse_args()
        item = Sales_data_model(
            # request_data["sid"],
            request_data["user_id"],
            request_data["product_id"],
            request_data["sale_amount"],
            request_data["date"],
        )

        try:
            item.save_to_db()
        except:
            return {
                "message": "An error occured while saving the sales data"
            }, 500  # internal server error

        return item.json(), 201

    def delete(self, sid):

        item = Sales_data_model.find_by_sid(sid)
        if item:
            item.delete_from_db()
        return {"message": "sales_data_deleted"}

    def put(self, sid):
        request_data = Sales_data.parser.parse_args()

        item = Sales_data_model.find_by_sid(sid)

        if item is None:
            item = Sales_data_model(
                # request_data["sid"],
                request_data["user_id"],
                request_data["product_id"],
                request_data["sale_amount"],
                request_data["date"],
            )
        else:

            item.user_id = request_data["user_id"]
            item.product_id = request_data["product_id"]
            item.sale_amount = request_data["sale_amount"]
            item.date = request_data["date"]
        item.save_to_db()

        return item.json()


class Sales_data_list(Resource):
    def get(self):
        return {"items": [item.json() for item in Sales_data_model.query.all()]}
