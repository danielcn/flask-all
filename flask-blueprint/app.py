from flask import Flask, Blueprint

from service1.service import service1
from service2.service import service2

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        app.register_blueprint(service1)
        app.register_blueprint(service2)

        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)