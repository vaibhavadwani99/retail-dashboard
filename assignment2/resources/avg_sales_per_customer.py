from flask_restful import Resource
from models.sales_data import Sales_data_model
from flask_jwt import jwt_required


class Average_sales(Resource):
    @jwt_required()
    def get(self, date):

        items = Sales_data_model.find_by_date(date)
        # the items which you are getting is an array of objects and each object represents the row of data
        sales = []
        unique_visitors = []
        for item in items:
            sales += [item.sale_amount]
            unique_visitors += [item.user_id]

        total_sales = sum(sales)
        visitors_unique = len(set(unique_visitors))
        return {"average sales per customer": total_sales / visitors_unique}
