from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


#patron saga
#orquestador 
#coreografia
#con orchesta hay delay, esto se soluciona con redis (db que actua como cache(?)

migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()

def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    f.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from .resources import payment
    app.register_blueprint(payment, url_prefix='/api/v1/payment')

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
            'db' : db
            }
    
    return app
