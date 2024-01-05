from app.models.expense import Expenses

class ExpensesController:
    # New method to fetch all expenses
    @staticmethod
    def get_all_expenses():
        return Expenses.get_all_expenses()
    
    # New method to fetch an expense
    @staticmethod
    def get_expense_by_id(expense_id):
        return Expenses.get_an_expense(expense_id)

        
    # New method to add an expense
    @staticmethod
    def add_expense(expense_type_id, description, amount, date, user_id):
        return Expenses.add_expense(expense_type_id, description, amount, date, user_id)
    
    
    # New method to update an expense
    @staticmethod
    def update_expense(expense_id, expense_type_id, description, amount, date, user_id):
        return Expenses.update_expense(expense_id, expense_type_id, description, amount, date, user_id)
    
    
    # New method to delete a expense
    @staticmethod
    def delete_expense(expense_id):
        return Expenses.delete_expense(expense_id)

