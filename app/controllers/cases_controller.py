from app.models.cases import Cases

class CasesController:
    # New method to fetch all cases
    @staticmethod
    def get_all_cases():
        return Cases.get_all_cases()
    
    # New method to fetch a case
    @staticmethod
    def get_case_by_id(case_id):
        return Cases.get_a_case(case_id)

        
    # New method to add a case
    @staticmethod
    def add_case(case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id):
        return Cases.add_case(case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id)
    
    
    # New method to update a case
    @staticmethod
    def update_case(case_id, case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id):
        return Cases.update_case(case_id, case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id)
    
    
    # New method to update a case issued aid
    @staticmethod
    def update_case_issued_aid(amount, cased_id):
        return Cases.update_case_issued_date(amount, cased_id)
    
    
    # New method to delete a case
    @staticmethod
    def delete_case(case_id):
        return Cases.delete_case(case_id)

