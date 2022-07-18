from flask_restful import Resource, reqparse
from models.average_sales_per_customer import Average_sales_model
import sqlite3


class Average_sales(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query1 = "SELECT sale_amount FROM sales_data"
        # query2 = "SELECT DISTINCT user_id FROM sales_data"
        result1 = cursor.execute(query1)
        # result2 = cursor.execute(query2)
        row1 = result1.fetchall()
        # row2 = result2.fetchall()
        connection.close()

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query2 = "SELECT DISTINCT user_id FROM sales_data"
        result2 = cursor.execute(query2)
        row2 = result2.fetchall()
        connection.close()

        # row is a list of tuples
        data = ()
        for i in range(0, len(row1)):
            data = data + row1[i]
        total_sales = sum(data)

        unique_visitors = len(row2)
        return {"average_sales_per_customer": (total_sales / unique_visitors)}
