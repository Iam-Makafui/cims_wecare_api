from flask import Flask
from app.routes.users_route import users_blueprint
from app.routes.roles_route import roles_blueprint
from app.routes.files_route import files_blueprint
from app.routes.members_route import members_blueprint
from app.routes.payment_type_route import paymenttypes_blueprint
from app.routes.payment_route import payment_blueprint
from app.routes.payment_amount_route import paymentamount_blueprint
from app.routes.payment_method_route import paymentmethod_blueprint
from app.routes.case_category_route import case_category_blueprint
from app.routes.cases_route import case_blueprint
from app.routes.query_route import query_blueprint  # Add new query blueprint
from app.auth_middleware import register_middleware
from app.db import db  # Import the SQLAlchemy instance

def create_app():
    app = Flask(__name__)
    
    # Configure PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/cims_dev'

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(users_blueprint)
    app.register_blueprint(roles_blueprint)
    app.register_blueprint(files_blueprint)
    app.register_blueprint(members_blueprint)
    app.register_blueprint(paymenttypes_blueprint)
    app.register_blueprint(payment_blueprint)
    app.register_blueprint(paymentamount_blueprint)
    app.register_blueprint(paymentmethod_blueprint)
    app.register_blueprint(case_category_blueprint)
    app.register_blueprint(case_blueprint)
    app.register_blueprint(query_blueprint)  # Register query blueprint
    
    register_middleware(app)

    return app

app = create_app()