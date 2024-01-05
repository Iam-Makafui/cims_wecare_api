from app.models.dues import Due

class DuesController:
    # New method to fetch all dues
    @staticmethod
    def get_all_dues():
        return Due.get_all_dues()
    
    # New method to fetch a due
    @staticmethod
    def get_due_by_id(due_id):
        return Due.get_a_due(due_id)

        
    # New method to add a due
    @staticmethod
    def add_due(member_id, amount, approval_status, payment_method, month_and_year, user_id):
        return Due.add_due(member_id, amount, approval_status, payment_method, month_and_year, user_id)
    
    
    # New method to update a due
    @staticmethod
    def update_due(due_id, member_id, amount, payment_method, month_and_year, user_id):
        return Due.update_due(due_id, member_id, amount, payment_method, month_and_year, user_id)
    
    
    # New method to update a due approval status
    @staticmethod
    def update_due_approval_status(approval_status, due_id):
        return Due.update_due_approval_status(approval_status, due_id)
    
    
    # New method to delete a due
    @staticmethod
    def delete_due(due_id):
        return Due.delete_due(due_id)

