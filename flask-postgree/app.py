from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'This is an app integration for Flask and Postgree db'
s
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)