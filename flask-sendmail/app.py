from flask import Flask, render_template, request
from send_mail import send_mail
from generate_token import generate_unique_link


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        send_mail("Messagge: {}".format(message))

@app.route('/confirm', methods=['POST'])
def confirm():
    generate_unique_link()
    return 'token validation'

if __name__ == '__main__':
    app.run()
