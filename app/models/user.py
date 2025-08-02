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
                    profiles.id, profiles.profile_id, profiles.first_name, profiles.last_name, profiles.email, profiles.profile_status, profiles.profile_type, profiles.cm_sys, profiles.cw_sys, profiles.ca_sys, profiles.w_sys, roles.role, profiles.inserted_at, profiles.profile_image, profiles.phone_number
                FROM 
                    profiles 
                INNER JOIN 
                    roles ON profiles.profile_type = roles.id 
                ORDER BY 
                    profiles.id DESC
            """)
        users = cursor.fetchall()
        cursor.close()
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
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET firstname = %s, lastname = %s, username = %s, email = %s, status = %s, role_id = %s, user_image = %s WHERE id = %s", 
                           (firstname, lastname, username, email, status, role_id, user_image, user_id,))
            connection.commit()
            cursor.close()
            return {'first_name': firstname, 'last_name': lastname, 'username': username, 'email': email, 'status': status, 'user_image': user_image}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None

        
    # method to update a user account details
    @staticmethod
    def update_password(password, user_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", 
                           (password, user_id,))
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'password': "Password Updated"}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a user    
    @staticmethod
    def delete_user(user_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to fetch a user
    @staticmethod
    def get_a_user(user_id):
        connection = db.engine.raw_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    profiles.id, profiles.profile_id, profiles.first_name, profiles.last_name, profiles.email, profiles.profile_status, profiles.profile_type, profiles.cm_sys, profiles.cw_sys, profiles.ca_sys, profiles.w_sys, roles.role, profiles.inserted_at, profiles.profile_image, profiles.phone_number
                FROM 
                    profiles 
                INNER JOIN 
                    roles ON profiles.profile_type = roles.id 
                WHERE 
                    profiles.id = %s 
                ORDER BY 
                    profiles.id DESC
            """, (user_id,))
            user = cursor.fetchone()
        return user
    
    
    # method to fetch a user by username and password
    @staticmethod
    def get_a_user_by_username_and_password(username, password):
        connection = db.engine.raw_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    profiles.id, profiles.profile_id, profiles.first_name, profiles.last_name, profiles.email, profiles.profile_status, profiles.profile_type, profiles.cm_sys, profiles.cw_sys, profiles.ca_sys, profiles.w_sys, roles.role, profiles.inserted_at, profiles.profile_image, profiles.phone_number
                FROM 
                    profiles 
                INNER JOIN 
                    roles ON profiles.profile_type = roles.id 
                WHERE 
                    profiles.email = %s 
                AND
                    profiles.password = %s
                ORDER BY 
                    profiles.id DESC
            """, (username, password,))
            user = cursor.fetchone()
        return user
    
    
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
    
    
    # method to add an authorization code
    @staticmethod
    def add_authorization_code(application_type, authorization_code):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO authorization_codes (application_type, code) VALUES (%s, %s)", (application_type, authorization_code,))
            connection.commit()
            cursor.close()
            return {'authorization_code': authorization_code, 'application_type': application_type}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
    
    # method to fetch an authorization code
    @staticmethod
    def get_an_authorization_code(application_type, authorization_code):
        connection = db.engine.raw_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    id, application_type, code, inserted_at, updated_at
                FROM 
                    authorization_codes 
                WHERE 
                    application_type = %s
                AND
                    code = %s 
                ORDER BY 
                    id DESC
            """, (application_type, authorization_code,))
            user = cursor.fetchone()
        return user
    
    
    

