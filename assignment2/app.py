from flask import Flask


from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.items import Item, item_list
from resources.total_sales import Total_sales
from resources.avg_sales_per_customer import Average_sales
from resources.unique_visitor import Unique_visitors
from resources.sales_data import Sales_data, Sales_data_list


from security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# this is turn off flask sqlalchemy tracking feature
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# in order to encrypt and understannd what is encrypted we require a key
app.secret_key = "vaibhav"

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


api.add_resource(Item, "/item/<int:pid>")
api.add_resource(item_list, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Total_sales, "/total_sales")
api.add_resource(Average_sales, "/average_sales")
api.add_resource(Unique_visitors, "/unique_visitors")
api.add_resource(Sales_data, "/sale/<int:sid>")
api.add_resource(Sales_data_list, "/sales")

if __name__ == "__main__":
    from db import db

    db.init_app(app)

    app.run(port=5000, debug=True)
