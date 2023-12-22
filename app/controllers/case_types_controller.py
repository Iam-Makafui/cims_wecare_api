from app.models.case_type import CaseType

class CaseTypesController:
    # New method to fetch all case types
    @staticmethod
    def get_all_case_types():
        return CaseType.get_all_case_types()
    
    # New method to fetch a case type
    @staticmethod
    def get_case_type_by_id(case_type_id):
        return CaseType.get_case_type_by_id(case_type_id)

        
    # New method to add a case type
    @staticmethod
    def add_case_type(case_type):
        return CaseType.add_case_type(case_type)
    
    
    # New method to update a case type
    @staticmethod
    def update_case_type(case_type_id, new_case_type):
        return CaseType.update_case_type(case_type_id, new_case_type)
    

    # New method to delete a case type
    @staticmethod
    def delete_case_type(case_type_id):
        return CaseType.delete_case_type(case_type_id)

