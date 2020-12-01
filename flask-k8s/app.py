from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return 'status 200 index', 200

@app.route('/error')
def error():
	return 'status 500 error', 500

@app.route('/success', methods=['GET'])
def success():
	return 'status 200 sucess', 200


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
