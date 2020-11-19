from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'This is an app wiht readness and liveness probe', 200 

@app.route('/readiness')
def index():
	return 'status', 200


@app.route('/liveness')
def index():
	return 'status', 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
