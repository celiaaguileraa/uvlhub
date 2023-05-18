import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.test_client()

    '''
    SETTING DATABASE CONNECTION
    #######################################
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOSTNAME')}:3306/{os.getenv('MYSQL_DATABASE')}"
    )
    db.init_app(app)

    '''
    REGISTERING ROUTES
    #######################################
    '''
    from app.tests.routes import test_routes
    app.register_blueprint(test_routes)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    '''
    REGISTERING MODELS
    #######################################
    '''

    from app.models import User
    migrate = Migrate(app, db)

    return app


def get_test_client():
    return create_app().test_client()