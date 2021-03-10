import src.helper as helper
from flask import Flask, request, Response

import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    helper.init_table()
    return 'Hello World!'


@app.route('/item/new', methods=['POST'])
def add_item():
    request_data = request.get_json()
    item = request_data['item']
    result_data = helper.add_to_list(item)
    if result_data is None:
        return Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
    return Response(json.dumps(result_data), mimetype='application/json')


@app.route('/items/all')
def get_all_items():
    result_data = helper.get_all_items()
    response = Response(json.dumps(result_data), mimetype='application/json')
    return response


@app.route('/item/status', methods=['GET'])
def get_status():
    item_name = request.args.get('name')
    status = helper.get_item_status(item_name)
    if status is None:
        return Response("{'error': 'Item Not Found - %s'}" % item_name, status=404, mimetype='application/json')
    result_data = {'status': status}
    return Response(json.dumps(result_data), status=200, mimetype='application/json')


@app.route('/item/update', methods=['PUT'])
def update_status():
    request_data = request.get_json()
    item = request_data['item']
    status = request_data['status']
    result_data = helper.update_status(item, status)
    if result_data is None:
        return Response("{'error': 'Error updating item - '" + item + ", " + status + "}",
                        status=400,
                        mimetype='application/json')
    return Response(json.dumps(result_data), mimetype='application/json')

