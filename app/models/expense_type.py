from app.db import mysql  

class ExpenseType:
    # method to fetch all expense types
    @staticmethod
    def get_all_expense_types():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM expense_types")
        expense_types = cursor.fetchall()
        cursor.close()
        return expense_types
    
    # method to fetch a expense type
    @staticmethod
    def get_expense_type_by_id(expense_type_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM expense_types WHERE id = %s", (expense_type_id,))
        expense_type = cursor.fetchone()
        cursor.close()
        return expense_type
    
    
    # method to add a expense type
    @staticmethod
    def add_expense_type(expense_type):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO expense_types (expense_type) VALUES (%s)", (expense_type,))
            mysql.connection.commit()
            cursor.close()
            return {'expense_type': expense_type}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a expense type
    @staticmethod
    def update_expense_type(expense_type_id, new_expense_type):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE expense_types SET expense_type = %s WHERE id = %s", (new_expense_type, expense_type_id))
            mysql.connection.commit()
            cursor.close()
            return {'expense_type_id': expense_type_id, 'expense_type': new_expense_type}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a expense type    
    @staticmethod
    def delete_expense_type(expense_type_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM expense_types WHERE id = %s", (expense_type_id,))
            mysql.connection.commit()
            cursor.close()
            return {'expense_type_id': expense_type_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


