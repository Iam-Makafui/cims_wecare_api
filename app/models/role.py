from app.db import mysql

class Role:
    # method to fetch all roles
    @staticmethod
    def get_all_roles():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM roles")
        roles = cursor.fetchall()
        cursor.close()
        return roles
    
    # method to add a role
    @staticmethod
    def add_role(role_name):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO roles (role_name) VALUES (%s)", (role_name,))
            mysql.connection.commit()
            cursor.close()
            return {'role_name': role_name}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None