from flask_restful import Resource
from models.sales_data import Sales_data_model


class Unique_visitors(Resource):
    def get(self, date):
        items = Sales_data_model.find_by_date(date)

        visitors = []
        for item in items:
            visitors += [item.user_id]

        return {"unique_visitors": len(set(visitors))}
