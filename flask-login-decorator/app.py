from flask import Flask, Response, request
from functools import wraps

app = Flask(__name__)
# app.config.from_object('settings')
app.config.from_pyfile('settings.py')


def valid_credentials(username, password):
    return username == app.config['USER'] and password == app.config['PASS']


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth.username or not auth.password or not valid_credentials(auth.username, auth.password):
            return Response('Login!', 401, {'WWW-Authenticate': 'Basic realm="Login!"'})
        return f(*args, **kwargs)

    return wrapper


@app.route('/secure', methods=['GET'])
@authenticate
def secure():
    return 'Secure!'


@app.route('/')
def index():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
