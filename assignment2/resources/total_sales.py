from flask_restful import Resource, reqparse

import sqlite3


class Total_sales(Resource):
    # parser = reqparse.RequestParser()

    # parser.add_argument(
    #     "name", type=str, required=True, help="this field cannot be blank"
    # )
    # parser.add_argument(
    #     "value", type=str, required=True, help="this field cannot be blank"
    # )

    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT sale_amount FROM sales_data"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()
        # row is a list of tuples
        data = ()
        for i in range(0, len(row)):
            data = data + row[i]
        total_sales = sum(data)
        return {"total_sales": total_sales}
