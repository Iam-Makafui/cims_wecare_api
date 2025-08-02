from flask import Blueprint, jsonify, request
from app.controllers.users_controller import UsersController

users_blueprint = Blueprint('users', __name__)

# route to fetch all roles
@users_blueprint.route('/users', methods=['GET'])
def get_users():
    users = UsersController.get_all_users()
    
    formatted_users = []
    for user in users:
        formatted_users.append({
            'id': user[0],
            'profile_id': user[1],
            'first_name': user[2],
            'last_name': user[3],
            'email': user[4],
            'status': user[5],
            'role_id': user[6],
            'cm_sys': user[7],
            'cw_sys': user[8],
            'ca_sys': user[9],
            'w_sys': user[10],
            'role_name': user[11],
            'created_at': user[12],
            'user_image': user[13],
            'phone_number': user[14]
        })
    
    return jsonify({'users': formatted_users})


# New route to add a user
@users_blueprint.route('/users', methods=['POST'])
def add_user():
    required_fields = ['profile_id', 'first_name', 'last_name', 'password', 'email', 'phone_number', 'status', 'role_id', 'user_image', 'cims_package', 'cm_sys', 'cw_sys', 'ca_sys', 'w_sys']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    profile_id = data['profile_id']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']
    email = data['email']
    phone_number = data['phone_number']
    status = data['status']
    role_id = data['role_id']
    user_image = data['user_image']
    cims_package = data['cims_package']
    cm_sys = data['cm_sys']
    cw_sys = data['cw_sys']
    ca_sys = data['ca_sys']
    w_sys = data['w_sys']

    # Call controller method to add user
    new_user = UsersController.add_user(profile_id, first_name, last_name, email, phone_number, password, status, role_id, user_image, cims_package, cm_sys, cw_sys, ca_sys, w_sys)
    
    if new_user:
        return jsonify({'message': 'User added successfully', 'user': new_user, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add user', 'status_code': 500}), 500
 
    
# New route to update a user profile details
@users_blueprint.route('/users/profile', methods=['PATCH'])
def update_user():
    required_fields = ['first_name', 'last_name', 'username', 'user_id', 'email', 'status', 'role_id', 'user_image']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    user_id = data['user_id']
    email = data['email']
    status = data['status']
    role_id = data['role_id']
    user_image = data['user_image']

    # Call controller method to update user profile details
    update_user = UsersController.update_user(user_id, first_name, last_name, username, email, status, role_id, user_image)
    
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
        return jsonify({'user': {'id': user[0], 'profile_id': user[1], 'first_name': user[2], 'last_name': user[3], 'email': user[4], 'status': user[5], 'role_id': user[6], 'cm_sys': user[7], 'cw_sys': user[8], 'ca_sys': user[9], 'w_sys': user[10], 'role_name': user[11], 'created_at': user[12], 'user_image': user[13], 'phone_number': user[14]} })
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 200
   
   
   
# Route to fetch a specific user by username and password
@users_blueprint.route('/users/<string:username>/<string:password>', methods=['GET'])
def get_a_user_by_username_and_password(username, password):
    user = UsersController.get_a_user_by_username_and_password(username, password)
    if user:
        return jsonify({'user': {'id': user[0], 'profile_id': user[1], 'first_name': user[2], 'last_name': user[3], 'email': user[4], 'status': user[5], 'role_id': user[6], 'cm_sys': user[7], 'cw_sys': user[8], 'ca_sys': user[9], 'w_sys': user[10], 'role_name': user[11], 'created_at': user[12], 'user_image': user[13], 'phone_number': user[14]}, 'status_code': 200 })
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 200
    

# Route to fetch last inserted profile
@users_blueprint.route('/recent/profile', methods=['GET'])
def get_last_inserted_profile():
    user = UsersController.get_last_inserted_profile()
    if user:
        return jsonify({'user': {'id': user[0], 'profile_id': user[1]}, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Profile table is empty', 'status_code': 404}), 200
    
    
# New route to add an authorization code
@users_blueprint.route('/authorization_code', methods=['POST'])
def add_authorization_code():
    required_fields = ['application_type', 'authorization_code']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    
    application_type = data['application_type']
    authorization_code = data['authorization_code']
    
   
    # Call controller method to add  an authorization code
    new_auth_code = UsersController.add_authorization_code(application_type, authorization_code)
    
    if new_auth_code:
        return jsonify({'message': 'Authorization code added successfully', 'authorization': new_auth_code, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add authorization code', 'status_code': 500}), 500
   
   
   
# Route to fetch an authorization code
@users_blueprint.route('/authorization_code/<string:application_type>/<int:authorization_code>', methods=['GET'])
def get_an_authorization_code(application_type, authorization_code):
    auth_code = UsersController.get_an_authorization_code(application_type, authorization_code)
    if auth_code:
        return jsonify({'authorization_code': {'id': auth_code[0], 'application_type': auth_code[1], 'code': auth_code[2], 'inserted_at': auth_code[3], 'updated_at': auth_code[4]}, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Authorization code not found', 'status_code': 404}), 200
    