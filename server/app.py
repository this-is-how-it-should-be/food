from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from food.html import html_code

from models import db, Food

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

CORS(app)

@app.route('/')
def this_is_how_food_should_be_webpage():
    return html_code

class AllFoods(Resource):
    
    def get(self):
        foods = Food.query.all()
        response_body = [food.to_dict() for food in foods]
        return make_response(response_body, 200)
    
api.add_resource(AllFoods, '/foods')

if __name__ == '__main__':
    app.run(port=4000, debug=True)