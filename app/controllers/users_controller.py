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
    def add_user(username, password, email, status, role_id, user_image):
        hashed_password = UsersController.hash_password(password)
        return User.add_user(username, hashed_password, email, status, role_id, user_image)
    
    # New method to update a user
    @staticmethod
    def update_user(user_id, username, email, status, role_id, user_image):
        return User.update_user(user_id, username, email, status, role_id, user_image)
    
    
    # New method to update a user account
    @staticmethod
    def update_password(password, user_id):
        hashed_password = UsersController.hash_password(password)
        return User.update_password(hashed_password, user_id)
    
    
    # New method to delete a role
    @staticmethod
    def delete_user(user_id):
        return User.delete_user(user_id)
    
    
    # New method to fetch a user
    @staticmethod
    def get_user_by_id(user_id):
        return User.get_a_user(user_id)