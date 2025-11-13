from flask import Flask, jsonify, request

app = Flask(__name__)


items = {}


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/item/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json(force=True)
    items[item_id] = data
    return jsonify({item_id: data}), 200


@app.route('/item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return '', 204
    return jsonify(error="Not found"), 404


if __name__ == '__main__':
    app.run(debug=True)
