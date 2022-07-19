from flask_restful import Resource, reqparse

import sqlite3


class Unique_visitors(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT DISTINCT user_id FROM sales_data "
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()
        # row is a list of tuples
        unique_visitors = len(row)
        return {"unique_visitors": unique_visitors}
