from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()
def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    migrate = Migrate(app, db)
    db.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app}
    
    return app