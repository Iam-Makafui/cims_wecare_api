from app.db import mysql  

class Due:
    # method to fetch all dues
    @staticmethod
    def get_all_dues():
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    members.member_id, members.name, dues.id, dues.amount, dues.approval_status, dues.payment_method, dues.month_and_year, dues.inserted_at, users.firstname, users.lastname
                FROM 
                    dues 
                INNER JOIN 
                    members on dues.member_id = members.id
                INNER JOIN 
                    users on dues.user_id = users.id
                ORDER BY 
                    dues.id DESC
            """)
            dues = cursor.fetchall()
        return dues
    
    # method to fetch a due
    @staticmethod
    def get_a_due(due_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    members.member_id, members.name, dues.id, dues.amount, dues.approval_status, dues.payment_method, dues.month_and_year, dues.inserted_at, users.firstname, users.lastname
                FROM 
                    dues 
                INNER JOIN 
                    members on dues.member_id = members.id
                INNER JOIN 
                    users on dues.user_id = users.id
                WHERE 
                    dues.id = %s 
                ORDER BY 
                    dues.id DESC
            """, (due_id,))
            dues = cursor.fetchone()
        return dues
    
    
    # method to add a due
    @staticmethod
    def add_due(member_id, amount, approval_status, payment_method, month_and_year, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO dues (member_id, amount, approval_status, payment_method, month_and_year, user_id) VALUES (%s, %s, %s, %s, %s, %s)",
                           (member_id, amount, approval_status, payment_method, month_and_year, user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'member_id': member_id, 'amount': amount, 'approval_status': approval_status, 'payment_method': payment_method, 'month_and_year': month_and_year, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a due
    @staticmethod
    def update_due(due_id, member_id, amount, payment_method, month_and_year, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE dues SET member_id = %s, amount = %s, payment_method = %s, month_and_year = %s, user_id = %s WHERE id = %s", 
                           (member_id, amount, payment_method, month_and_year, user_id, due_id,))
            mysql.connection.commit()
            cursor.close()
            return {'member_id': member_id, 'amount': amount, 'payment_method': payment_method, 'month_and_year': month_and_year, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
    
    # method to update a due approval status
    @staticmethod
    def update_due_approval_status(approval_status, due_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE dues SET approval_status = %s WHERE id = %s", 
                           (approval_status, due_id,))
            mysql.connection.commit()
            cursor.close()
            return {'dues': "Approval Status Updated"}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None    
    
        
    # method to delete a due    
    @staticmethod
    def delete_due(due_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM dues WHERE id = %s", (due_id,))
            mysql.connection.commit()
            cursor.close()
            return {'due_id': due_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


