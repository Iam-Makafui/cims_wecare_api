from app.models.role import Role

class RolesController:
    # New method to fetch all roles
    @staticmethod
    def get_all_roles():
        return Role.get_all_roles()
    
    # New method to add a role
    @staticmethod
    def add_role(role_name):
        return Role.add_role(role_name)