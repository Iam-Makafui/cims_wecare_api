from app.models.user import User
import hashlib

class UsersController:
    #method for hashing passwords    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # New method to fetch all users
    @staticmethod
    def get_all_users():
        return User.get_all_users()
    
    # New method to add a user
    @staticmethod
    def add_user(profile_id, firstname, lastname, email, phone_number, password, status, role_id, user_image, cims_package, cm_sys, cw_sys, ca_sys, w_sys):
        hashed_password = UsersController.hash_password(password)
        return User.add_user(profile_id, firstname, lastname, email, phone_number, hashed_password, status, role_id, user_image, cims_package, cm_sys, cw_sys, ca_sys, w_sys)
    
    # New method to update a user
    @staticmethod
    def update_user(user_id, firstname, lastname, username, email, status, role_id, user_image):
        return User.update_user(user_id, firstname, lastname, username, email, status, role_id, user_image)
    
    
    # New method to update a user account
    @staticmethod
    def update_password(password, user_id):
        hashed_password = UsersController.hash_password(password)
        return User.update_password(hashed_password, user_id)
    
    
    # New method to delete a role
    @staticmethod
    def delete_user(user_id):
        return User.delete_user(user_id)
    
    
    # New method to fetch a user by id
    @staticmethod
    def get_user_by_id(user_id):
        return User.get_a_user(user_id)
    
    # New method to fetch a user by username and password
    @staticmethod
    def get_a_user_by_username_and_password(username, password):
        hashed_password = UsersController.hash_password(password)
        return User.get_a_user_by_username_and_password(username, hashed_password)
    
    # New method to fetch last inserted profile
    @staticmethod
    def get_last_inserted_profile():
        return User.get_last_inserted_profile()
    
    
    # New method to add an authorization code
    @staticmethod
    def add_authorization_code(application_type, authorization_code):
        return User.add_authorization_code(application_type, authorization_code)
    
    
    # New method to get an authorization code
    @staticmethod
    def get_an_authorization_code(application_type, authorization_code):
        return User.get_an_authorization_code(application_type, authorization_code)
    
    
    
    # method for updating user status
    @staticmethod
    def update_user_status(user_id, new_status):
        return User.update_user_status(user_id, new_status)