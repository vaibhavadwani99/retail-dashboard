import sqlite3
from flask import Flask
from flask_cors import CORS


from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from resources.wine import QualityCountPlot

# from resources.wine import AlcoholHistogram
from resources.wine import SulphurScatter
from resources.wine import densityPhScatter
from resources.wine import LabelCountPlot

# from resources.items import Item, item_list
# from resources.total_sales import Total_sales
# from resources.avg_sales_per_customer import Average_sales
# from resources.unique_visitor import Unique_visitors
# from resources.sales_data import Sales_data, Sales_data_list


from security import authenticate, identity

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wine.db"
# this is turn off flask sqlalchemy tracking feature
# sqlalchemy will track the wine.db database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# in order to encrypt and understannd what is encrypted we require a key
app.secret_key = "vaibhav"

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


api.add_resource(UserRegister, "/register")
api.add_resource(QualityCountPlot, "/qcount_plot")
# api.add_resource(AlcoholHistogram, "/ahist_plot")
api.add_resource(SulphurScatter, "/s_scatter_plot")
api.add_resource(densityPhScatter, "/densityPh_scatter_plot")
api.add_resource(LabelCountPlot, "/label_count")


if __name__ == "__main__":
    from db import db
    import pandas as pd
    from pathlib import Path

    Path("wine.db").touch()  # this makes an empty wine.db file

    connection = sqlite3.connect("wine.db")
    cursor = connection.cursor()

    wine_data = pd.read_csv("./dataset/winequality-red.csv")
    # writing the data to the sql table
    wine_data.to_sql("wine", connection, if_exists="replace", index=False)

    connection.commit()
    connection.close()

    db.init_app(app)

    app.run(port=5000, debug=True)
