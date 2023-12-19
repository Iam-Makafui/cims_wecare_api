from flask import Blueprint, jsonify, request
from app.controllers.roles_controller import RolesController

roles_blueprint = Blueprint('roles', __name__)

# route to fetch all roles
@roles_blueprint.route('/roles', methods=['GET'])
def get_roles():
    roles = RolesController.get_all_roles()
    return jsonify({'roles': roles})



# New route to add a role
@roles_blueprint.route('/roles', methods=['POST'])
def add_role():
    role_name = request.json.get('role_name')
    if not role_name:
        return jsonify({'error': 'Role name is required'}), 400
    
    # Call controller method to add role
    new_role = RolesController.add_role(role_name)
    
    if new_role:
        return jsonify({'message': 'Role added successfully', 'role': new_role}), 201
    else:
        return jsonify({'error': 'Failed to add role'}), 500