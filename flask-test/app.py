from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # LoggerHandler.log_info('Hello, world!')
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)