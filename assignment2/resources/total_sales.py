from flask_restful import Resource
from flask_jwt import jwt_required

from models.sales_data import Sales_data_model


class Total_sales(Resource):
    @jwt_required()
    def get(self, date):
        items = Sales_data_model.find_by_date(date)
        sales = []
        for item in items:
            sales += [item.sale_amount]
        return {"total sales": sum(sales)}
