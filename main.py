from src.helper import add_to_list, init_table
from flask import Flask, request, Response

import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    init_table()
    return 'Hello World!'


@app.route('/item/new', methods=['POST'])
def add_item():
    request_data = request.get_json()
    item = request_data['item']
    result_data = add_to_list(item)
    if result_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
        return response
    response = Response(json.dumps(result_data), mimetype='application/json')
    return response


