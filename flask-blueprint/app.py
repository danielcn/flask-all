from flask import Flask, Blueprint

from .service1 import service1
from .service1 import service2

service1 = Blueprint('service1', __name__)
service2 = Blueprint('service2', __name__)

app = Flask()
app.register_blueprint(service1)
app.register_blueprint(service2)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)