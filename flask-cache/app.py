# from flask import Flask
# from flask_caching import Cache

# cache = Cache()

# def create_app():
#   app = Flask(__name__)

#   app.config['CACHE_TYPE'] = 'simple'
#   cache.init_app(app)

#   return app

# # app = create_app()

# @app.route('/')
# # @cache.cached(timout=10)
# def index():
#   randnum=raninit(1,1000)
#   return f'<h1>The number is:{randnum}<h1>'


# def calculate():
#   return


from flask import Flask
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


@app.route('/')
@cache.cached(timeout=50)
def index():
    return 'Cached for 50s'


https://www.youtube.com/watch?v=iO0sL6Vyfps&feature=em-uploademail