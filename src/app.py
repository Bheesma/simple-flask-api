
from urllib import request
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

#------------------------------------------------------------


@app.route('/', methods=['GET'])
def index():
    resp = {'name': 'HelloWorld'}
    return jsonify(resp)

#------------------------------------------------------------


@app.route('/add', methods=['GET'])
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    resp = {'sum': a+b}
    return jsonify(resp)

#------------------------------------------------------------

@app.route('/customer/<id>', methods=['GET'])
def customer(id):

    resp = {
        'customerId': id,
        'firstName': 'Jack',
        'lastName': 'Sparrow',
        'city': 'Melbourne',
        'interests': ['Swimming', 'Adventure', 'Travel']
    }
    return jsonify(resp)

#------------------------------------------------------------


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
