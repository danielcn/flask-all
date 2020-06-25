from flask import Flask, Blueprint

app = Flask()
app.register_blueprint()
app.register_blueprint()

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)