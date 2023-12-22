from flask import Flask
from app.routes.roles_route import roles_blueprint
from app.routes.users_route import users_blueprint
from app.routes.members_route import members_blueprint
from app.routes.case_types_route import case_types_blueprint
from app.routes.cases_route import cases_blueprint
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
    
    #roles blueprint
    app.register_blueprint(roles_blueprint)
    #user blueprint
    app.register_blueprint(users_blueprint)
    #members blueprint
    app.register_blueprint(members_blueprint)
    #case type blueprint
    app.register_blueprint(case_types_blueprint)
    #cases blueprint
    app.register_blueprint(cases_blueprint)
    
    register_middleware(app)

    return app

app = create_app()