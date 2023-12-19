from flask import Flask

app = Flask(__name__)

from app.routes.roles_management import roles_blueprint  # Import after creating the app instance

# Register blueprint
app.register_blueprint(roles_blueprint)