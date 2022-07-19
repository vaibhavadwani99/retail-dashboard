from flask_restful import Resource, reqparse

import sqlite3


class Total_sales(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT SUM(sale_amount) FROM sales_data"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()

        return {"total_sales": row[0][0]}
