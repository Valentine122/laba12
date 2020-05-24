from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String

import copy
import json

from app.models.bar import Bar

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(user=SECRET["user"],
                                                                              password=SECRET["password"],
                                                                              host=SECRET["host"],
                                                                              port=SECRET["port"],
                                                                              db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Bar_py(Bar, db.Model):
    id = Column(Integer, primary_key=True)
    bar_name = db.Column(String(50), unique=False)
    price_in_uah = Column(Integer, unique=False)
    production_year = Column(Integer, unique=False)
    barman = Column(String(50), unique=False)
    shapeOfIce = Column(String(50), unique=False)
    location = Column(String(50), unique=False)

    def __init__(self, bar_name="N/A", price_in_uah=0, barman="UNKNOWN", production_year=2005, shapeOfIce="Ghost", location="N/A"):
        super().__init__(bar_name, price_in_uah, barman, production_year)
        self.shapeOfIce = shapeOfIce
        self.location = location


class BarSchema(ma.Schema):
    class Meta:
        fields = ('bar_name', 'price_in_uah', 'barman', 'production_year', 'shapeOfIce', 'location')


bar_schema = BarSchema()
bars_schema = BarSchema(many=True)


@app.route("/barpy", methods=["POST"])
def add_bar_py():
    bar_name = request.json['bar_name']
    price_in_uah = request.json['price_in_uah']
    barman = request.json['barman']
    production_year = request.json['production_year']
    shapeOfIce = request.json['shapeOfIce']
    location = request.json['location']
    bar_py = Bar_py(bar_name, price_in_uah, barman, production_year, shapeOfIce, location)

    db.session.add(bar_py)
    db.session.commit()
    return bar_schema.jsonify(bar_py)


@app.route("/barpy", methods=["GET"])
def get_bars_py():
    all_bar_py = Bar_py.query.all()
    result = bars_schema.dump(all_bar_py)
    return jsonify({'bar_py': result})


@app.route("/barpy/<id>", methods=["GET"])
def get_bar_py(id):
    bar_py = Bar_py.query.get(id)
    if not bar_py:
        abort(404)
    return bar_schema.jsonify(bar_py)


@app.route("/barpy/<id>", methods=["PUT"])
def update_bar_py(id):
    bar_py = Bar_py.query.get(id)
    if not bar_py:
        abort(404)
    old_bar_py = copy.deepcopy(bar_py)
    bar_py.bar_name = request.json['bar_name']
    bar_py.price_in_uah = request.json['price_in_uah']
    bar_py.production_year = request.json['production_year']
    bar_py.barman = request.json['barman']
    bar_py.shapeOfIce = request.json['shapeOfIce']
    bar_py.location = request.json['location']
    db.session.commit()
    return bar_schema.jsonify(old_bar_py)


@app.route("/barpy/<id>", methods=["DELETE"])
def delete_bar_py(id):
    bar_py = Bar_py.query.get(id)
    if not bar_py:
        abort(404)
    db.session.delete(bar_py)
    db.session.commit()
    return bar_schema.jsonify(bar_py)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')