from flask import Flask

from food.html import html_code
from food.data.foods import foods

app = Flask(__name__)

@app.route('/')
def this_is_how_food_should_be_webpage():
    return html_code

@app.route('/foods')
def get_foods():
    return foods

if __name__ == '__main__':
    app.run(port=4000, debug=True)