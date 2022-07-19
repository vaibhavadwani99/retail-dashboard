from flask_restful import Resource, reqparse

import sqlite3


class Average_sales(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query1 = "SELECT user_id, SUM(sale_amount) FROM sales_data GROUP BY user_id"

        result1 = cursor.execute(query1)

        row1 = result1.fetchall()

        connection.close()

        data = 0
        for i in range(0, len(row1)):
            data = data + row1[i][1]

        unique_visitors = len(row1)
        return {"average_sales_per_customer": data / unique_visitors}
