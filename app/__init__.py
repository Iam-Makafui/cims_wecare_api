from flask import Flask
from app.routes.roles_management import roles_blueprint
from app.auth_middleware import register_middleware
from app.db import mysql  # Import the MySQL instance

def create_app():
    app = Flask(__name__)

    # Configure MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'welfare_management_system_dev'

    # Initialize MySQL
    mysql.init_app(app)

    # Register blueprints, middleware, etc.
    app.register_blueprint(roles_blueprint)
    register_middleware(app)

    return app

app = create_app()