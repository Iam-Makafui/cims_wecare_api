from app.models.role import Role

class RolesController:
    # New method to fetch all roles
    @staticmethod
    def get_all_roles():
        return Role.get_all_roles()
    
    # New method to fetch a role
    @staticmethod
    def get_role_by_id(role_id):
        return Role.get_role_by_id(role_id)

        
    # New method to add a role
    @staticmethod
    def add_role(role_name):
        return Role.add_role(role_name)
    
    
    # New method to update a role
    @staticmethod
    def update_role(role_id, new_role_name):
        return Role.update_role(role_id, new_role_name)
    
    
    # New method to delete a role
    @staticmethod
    def delete_role(role_id):
        return Role.delete_role(role_id)

