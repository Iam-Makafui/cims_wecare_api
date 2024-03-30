# from app.db import mysql
from app.db import db  # Import the SQLAlchemy instance  

class User:
    # method to fetch all users
    @staticmethod
    def get_all_users():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    profiles.id, profiles.first_name, profiles.last_name, profiles.email, profiles.profile_status, profiles.profile_type, profiles.cm_sys, profiles.cw_sys, profiles.ca_sys, profiles.w_sys, roles.id, roles.role, profiles.inserted_at, profiles.profile_image
                FROM 
                    profiles 
                INNER JOIN 
                    roles ON profiles.profile_type = roles.id 
                ORDER BY 
                    profiles.id DESC
            """)
        users = cursor.fetchall()
            
        return users
    
    
    # method to add a user
    @staticmethod
    def add_user(profile_id, firstname, lastname, email, phone_number, password, status, role_id, user_image, cims_package, cm_sys, cw_sys, ca_sys, w_sys):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO profiles (profile_id, first_name, last_name, email, phone_number, password, profile_status, profile_type, profile_image, cims_package, cm_sys, cw_sys, ca_sys, w_sys) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (profile_id, firstname, lastname, email, phone_number, password, status, role_id, user_image, cims_package, cm_sys, cw_sys, ca_sys, w_sys,))
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'profile_id': profile_id, 'first_name': firstname, 'last_name': lastname, 'email': email, phone_number: phone_number, 'status': status, 'image': user_image}
        except Exception as e:
             print(e)  # Handle the exception according to your application's error handling
             return None

        
    # method to update a user profile details
    @staticmethod
    def update_user(user_id, firstname, lastname, username, email, status, role_id, user_image):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE users SET firstname = %s, lastname = %s, username = %s, email = %s, status = %s, role_id = %s, user_image = %s WHERE id = %s", 
                           (firstname, lastname, username, email, status, role_id, user_image, user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'first_name': firstname, 'last_name': lastname, 'username': username, 'email': email, 'status': status, 'user_image': user_image}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None

        
    # method to update a user account details
    @staticmethod
    def update_password(password, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", 
                           (password, user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'password': "Password Updated"}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a user    
    @staticmethod
    def delete_user(user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to fetch a user
    # @staticmethod
    # def get_a_user(user_id):
    #     with mysql.connection.cursor() as cursor:
    #         cursor.execute("""
    #             SELECT 
    #                 users.id, users.firstname, users.lastname, users.username, users.email, users.status, roles.id, roles.role_name, users.created_at, users.user_image
    #             FROM 
    #                 users
    #             INNER JOIN 
    #                 roles ON users.role_id = roles.id 
    #             WHERE 
    #                 users.id = %s 
    #             ORDER BY 
    #                 users.id DESC
    #         """, (user_id,))
    #         user = cursor.fetchone()
    #     return user
    
    
    # method to fetch a user
    @staticmethod
    def get_last_inserted_profile():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    profiles.id, profiles.profile_id
                FROM 
                    profiles
                ORDER BY 
                    profiles.id DESC LIMIT 1
            """)
        user = cursor.fetchone()
        return user
    
    
    

