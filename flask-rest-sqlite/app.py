from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {"id": self.id,
                "name": self.name}


@app.route('/user/', methods=['GET'])
def index():
    return jsonify({'users': list(map(lambda user: user.serialize(), User.query.all()))})


@app.route('/user/<int:id>/')
def get_dev(id):
    return jsonify({'user': User.query.get(id).serialize()})


@app.route('/user/', methods=['POST'])
def create_dev():
    if not request.json or not 'name' in request.json:
        abort(400)
    dev = User(request.json['name'])
    db.session.add(dev)
    db.session.commit()
    return jsonify({'user': user.serialize()}), 201


@app.route('/user/<int:id>/', methods=['DELETE'])
def delete_dev(id):
    db.session.delete(User.query.get(id))
    db.session.commit()
    return jsonify({'result': True})


@app.route('/user/<int:id>/', methods=['PUT'])
def update_dev(id):
    dev = User.query.get(id)
    user.name = request.json.get('name', user.name)
    db.session.commit()
    return jsonify({'dev': user.serialize()})