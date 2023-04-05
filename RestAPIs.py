from flask import Flask, request, jsonify, json

app = Flask(__name__)

items = [
    {"name": "Coke", "category": 1, "price": 20.5, "instock": 200},
    {"name": "Sprite", "category": 2, "price": 15, "instock": 220},
    {"name": "Pepsi", "category": 3, "price": 29, "instock": 300},
]
def _find_next_name(name):
    data = [x for x in items if x['name'] == name]
    return data

print(_find_next_name("Coke"))

@app.route('/items/<name>', methods=["DELETE"])
def delete_item(name: str):

    data = _find_next_name(name)
    if not data:
        return {"error": "Items not found"}, 404
    else:
        items.remove(data[0])
        return "Items delete successfully", 200

#RESt
@app.route('/items', methods=["GET"])
def get_item():
    return jsonify(items)

#GEt
@app.route('/item/<name>', methods=["GET"])
def get_items_name(name):
    data = _find_next_name(name)
    return jsonify(data)

#POSt
@app.route('/items', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
        
    }

    if (_find_next_name(name) == name):
        return {"error": "Bad Request!"}, name
    else:
        items.append(new_data)
        return jsonify(items)

#PUt
@app.route('/items/<name>', methods=["PUT"])
def update_item(name):
    global items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')


    for items in items:
        if name == items["name"]:
            items["category"] = int(category)
            items["price"] = int(price)
            items["instock"] = int(instock)
            return jsonify(items)

    else:
        return "Error", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)