from flask import Flask
from flask_caching import Cache

config = {
    "DEBUG": True,         
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=50)
def index():
    return 'Cached for 50s'

if __name__ == '__main__':
    app.run(port=5000, debug=True)

