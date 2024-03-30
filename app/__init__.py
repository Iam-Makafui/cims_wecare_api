from flask import Flask
from app.routes.users_route import users_blueprint
from app.routes.files_route import files_blueprint
from app.auth_middleware import register_middleware
# from app.db import mysql  # Import the MySQL instance
from app.db import db  # Import the SQLAlchemy instance

def create_app():
    app = Flask(__name__)
    
    # Configure PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/church_administrative_db_dev'

    # Initialize SQLAlchemy
    db.init_app(app)

    app.register_blueprint(users_blueprint)
    app.register_blueprint(files_blueprint)
    
    register_middleware(app)

    return app

app = create_app()