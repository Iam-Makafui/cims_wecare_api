from flask import Blueprint, jsonify, request
from app.controllers.users_controller import UsersController

users_blueprint = Blueprint('users', __name__)

# route to fetch all roles
@users_blueprint.route('/users', methods=['GET'])
def get_users():
    roles = UsersController.get_all_users()
    
    formatted_users = []
    for role in roles:
        formatted_users.append({
            'id': role[0],
            'username': role[1],
            'email': role[2],
            'status': role[3],
            'role_id': role[4],
            'role_name': role[5],
            'created_at': role[6],
            'user_image': role[7]
        })
    
    return jsonify({'users': formatted_users})


# New route to add a user
@users_blueprint.route('/users', methods=['POST'])
def add_user():
    required_fields = ['username', 'password', 'email', 'status', 'role_id', 'user_image']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    username = data['username']
    password = data['password']
    email = data['email']
    status = data['status']
    role_id = data['role_id']
    user_image = data['user_image']

    # Call controller method to add user
    new_user = UsersController.add_user(username, password, email, status, role_id, user_image)
    
    if new_user:
        return jsonify({'message': 'User added successfully', 'user': new_user, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add user', 'status_code': 500}), 500
 
    
# New route to update a user profile details
@users_blueprint.route('/users/profile', methods=['PATCH'])
def update_user():
    required_fields = ['username', 'user_id', 'email', 'status', 'role_id', 'user_image']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    username = data['username']
    user_id = data['user_id']
    email = data['email']
    status = data['status']
    role_id = data['role_id']
    user_image = data['user_image']

    # Call controller method to update user profile details
    update_user = UsersController.update_user(user_id, username, email, status, role_id, user_image)
    
    if update_user:
        return jsonify({'message': 'User Profile Updated Successfully', 'user': update_user, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update user', 'status_code': 500}), 500



# New route to update a user account details
@users_blueprint.route('/users/account', methods=['PATCH'])
def update_password():
    required_fields = ['password', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    password = data['password']
    user_id = data['user_id']

    # Call controller method to update user account details
    update_user_account = UsersController.update_password(password, user_id)
    
    if update_user_account:
        return jsonify({'message': 'User Password Updated Successfully', 'user': update_user_account, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update user', 'status_code': 500}), 500
    
    
    
# New route to delete a user
@users_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    deleted_user = UsersController.delete_user(user_id)
    
    if deleted_user:
        return jsonify({'message': f'User with ID {user_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete user with ID {user_id}', 'status_code': 500}), 500
    

# Route to fetch a specific user by ID
@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UsersController.get_user_by_id(user_id)
    if user:
        return jsonify({'user': {'id': user[0], 'username': user[1], 'email': user[2], 'status': user[3], 'role_id': user[4], 'role_name': user[5], 'created_at': user[6], 'user_image': user[7]} })
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404