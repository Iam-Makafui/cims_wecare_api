from app.models.cases import Case

class CasesController:
    # New method to fetch all cases
    @staticmethod
    def get_all_cases():
        return Case.get_all_cases()
    
    # New method to fetch a case
    @staticmethod
    def get_case_by_id(case_id):
        return Case.fetch_a_case(case_id)
    
    
    # New method to fetch a case
    @staticmethod
    def fetch_all_cases_by_status(case_status):
        return Case.fetch_all_cases_by_status(case_status)

        
    # New method to add a case
    @staticmethod
    def add_case(case_id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by):
        return Case.add_case(case_id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by)
    
    
    # New method to update a case
    @staticmethod
    def update_case(id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by):
        return Case.update_case(id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by)
    
    
    # New method to update a case status
    @staticmethod
    def update_case_status(id, case_status):
        return Case.update_case_status(id, case_status)
    
    
    # New method to delete a case
    @staticmethod
    def delete_case(case_id):
        return Case.delete_case(case_id)
    
    
    # New method to fetch last inserted case
    @staticmethod
    def get_last_inserted_case():
        return Case.get_last_inserted_case()

