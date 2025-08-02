# from app.db import mysql
from app.db import db  # Import the SQLAlchemy instance  


class Role:
    # method to fetch all roles
    @staticmethod
    def get_all_roles():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT * FROM roles
            """)
        roles = cursor.fetchall()
        cursor.close()
        return roles
    
    # method to fetch a role
    @staticmethod
    def get_role_by_id(role_id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roles WHERE id = %s", (role_id,))
        role = cursor.fetchone()
        cursor.close()
        return role
    
    
    # method to add a role
    @staticmethod
    def add_role(role_name):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO roles (role) VALUES (%s)", (role_name,))
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'role_name': role_name}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a role
    @staticmethod
    def update_role(role_id, new_role_name):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE roles SET role = %s WHERE id = %s", (new_role_name, role_id))
            connection.commit()
            cursor.close()
            connection.close()
            return {'role_id': role_id, 'new_role_name': new_role_name}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a role    
    @staticmethod
    def delete_role(role_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM roles WHERE id = %s", (role_id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'role_id': role_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


