from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	return 'status 200 on index', 200 

@app.route('/error')
def index():
	return 'status 500 error', 500 

@app.route('/', methods=['POST'])
def index():
	return 'status 200 on index', 200 

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
