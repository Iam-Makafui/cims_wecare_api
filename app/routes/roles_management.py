from flask import Blueprint, jsonify, request
from app.controllers.roles_controller import RolesController

roles_blueprint = Blueprint('roles', __name__)

# route to fetch all roles
@roles_blueprint.route('/roles', methods=['GET'])
def get_roles():
    roles = RolesController.get_all_roles()
    
    formatted_roles = []
    for role in roles:
        formatted_roles.append({
            'id': role[0],
            'role_name': role[1],
            'inserted_at': role[2],
            'updated_at': role[3]
        })
    
    return jsonify({'roles': formatted_roles})


# Route to fetch a specific role by ID
@roles_blueprint.route('/roles/<int:role_id>', methods=['GET'])
def get_role_by_id(role_id):
    role = RolesController.get_role_by_id(role_id)
    if role:
        return jsonify({'role': {'id': role[0], 'role_name': role[1], 'inserted_at': role[2], 'updated_at': role[3]} })
    else:
        return jsonify({'error': 'Role not found', 'status_code': 404}), 404


# New route to add a role
@roles_blueprint.route('/roles', methods=['POST'])
def add_role():
    role_name = request.json.get('role_name')
    if not role_name:
        return jsonify({'error': 'Role name is required', 'status_code': 400}), 400
    
    # Call controller method to add role
    new_role = RolesController.add_role(role_name)
    
    if new_role:
        return jsonify({'message': 'Role added successfully', 'role': new_role, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add role', 'status_code': 500}), 500
    
    
# New route to update a role  
@roles_blueprint.route('/roles/<int:role_id>', methods=['PATCH'])
def update_role_by_id(role_id):
    new_role_name = request.json.get('role_name')
    if not new_role_name:
        return jsonify({'error': 'New role name is required', 'status_code': 400}), 400

    updated_role = RolesController.update_role(role_id, new_role_name)
    
    if updated_role:
        return jsonify({'message': f'Role with ID {role_id} updated successfully', 'role': updated_role, 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to update role with ID {role_id}', 'status_code': 500}), 500



# New route to delete a role
@roles_blueprint.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role_by_id(role_id):
    deleted_role = RolesController.delete_role(role_id)
    
    if deleted_role:
        return jsonify({'message': f'Role with ID {role_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete role with ID {role_id}', 'status_code': 500}), 500
