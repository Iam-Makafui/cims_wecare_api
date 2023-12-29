from app.models.expense_type import ExpenseType

class ExpenseTypesController:
    # New method to fetch all expense types
    @staticmethod
    def get_all_expense_types():
        return ExpenseType.get_all_expense_types()
    
    # New method to fetch a expense type
    @staticmethod
    def get_expense_type_by_id(expense_type_id):
        return ExpenseType.get_expense_type_by_id(expense_type_id)

        
    # New method to add a expense type
    @staticmethod
    def add_expense_type(expense_type):
        return ExpenseType.add_expense_type(expense_type)
    
    
    # New method to update a expense type
    @staticmethod
    def update_expense_type(expense_type_id, new_expense_type):
        return ExpenseType.update_expense_type(expense_type_id, new_expense_type)
    

    # New method to delete a expense type
    @staticmethod
    def delete_expense_type(expense_type_id):
        return ExpenseType.delete_expense_type(expense_type_id)

