from app.db import mysql  

class User:
    # method to fetch all users
    @staticmethod
    def get_all_users():
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    users.id, users.firstname, users.lastname, users.username, users.email, users.status, roles.id, roles.role_name, users.created_at, users.user_image
                FROM 
                    users 
                INNER JOIN 
                    roles ON users.role_id = roles.id 
                ORDER BY 
                    users.id DESC
            """)
            users = cursor.fetchall()
        return users
    
    
    # method to add a user
    @staticmethod
    def add_user(firstname, lastname, username, password, email, status, role_id, user_image):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users (firstname, lastname, username, password, email, status, role_id, user_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (firstname, lastname, username, password, email, status, role_id, user_image,))
            mysql.connection.commit()
            cursor.close()
            return {'first_name': firstname, 'last_name': lastname, 'username': username, 'email': email, 'status': status, 'image': user_image}
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
    @staticmethod
    def get_a_user(user_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    users.id, users.firstname, users.lastname, users.username, users.email, users.status, roles.id, roles.role_name, users.created_at, users.user_image
                FROM 
                    users
                INNER JOIN 
                    roles ON users.role_id = roles.id 
                WHERE 
                    users.id = %s 
                ORDER BY 
                    users.id DESC
            """, (user_id,))
            user = cursor.fetchone()
        return user

