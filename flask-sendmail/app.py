from flask import Flask, render_template, request
from send_mail import send_mail

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        send_mail("Messagge: {}".format(message))

if __name__ == '__main__':
    app.run()
