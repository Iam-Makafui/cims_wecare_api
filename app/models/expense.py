from app.db import mysql  

class Expenses:
    # method to fetch all expenses
    @staticmethod
    def get_all_expenses():
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    expense_types.expense_type, expenses.id, expenses.description, expenses.amount, expenses.date, expenses.inserted_at, users.firstname, users.lastname
                FROM 
                    expenses 
                INNER JOIN 
                    expense_types on expenses.expense_type_id = expense_types.id
                INNER JOIN
                    users on expenses.user_id = users.id
                ORDER BY 
                    expenses.id DESC
            """)
            expenses = cursor.fetchall()
        return expenses
    
    
    # method to fetch an expense
    @staticmethod
    def get_an_expense(expense_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    expense_types.expense_type, expenses.id, expenses.description, expenses.amount, expenses.date, expenses.inserted_at, users.firstname, users.lastname
                FROM 
                    expenses 
                INNER JOIN 
                    expense_types on expenses.expense_type_id = expense_types.id
                INNER JOIN
                    users on expenses.user_id = users.id
                WHERE 
                    expenses.id = %s 
                ORDER BY 
                    expenses.id DESC
            """, (expense_id,))
            expense = cursor.fetchone()
        return expense
    
    
    # method to add an expense
    @staticmethod
    def add_expense(expense_type_id, description, amount, date, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO expenses (expense_type_id, description, amount, date, user_id) VALUES (%s, %s, %s, %s, %s)",
                           (expense_type_id, description, amount, date, user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'expense_type_id': expense_type_id, 'description': description, 'amount': amount, 'date': date, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a expense
    @staticmethod
    def update_expense(expense_id, expense_type_id, description, amount, date, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE expenses SET expense_type_id = %s, description = %s, amount = %s, date = %s, user_id = %s WHERE id = %s", 
                           (expense_type_id, description, amount, date, user_id, expense_id,))
            mysql.connection.commit()
            cursor.close()
            return {'expense_type_id': expense_type_id, 'description': description, 'amount': amount, 'date': date, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None

        
    # method to delete an expense    
    @staticmethod
    def delete_expense(expense_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
            mysql.connection.commit()
            cursor.close()
            return {'expense_id': expense_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


