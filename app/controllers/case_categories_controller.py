from app.models.case_categories import CaseCategory

class CaseCategoriesController:
    # New method to fetch all case categories
    @staticmethod
    def get_all_case_caetegories():
        return CaseCategory.get_all_case_caetegories()
    
    # New method to fetch a case category
    @staticmethod
    def get_case_category_by_id(case_category_id):
        return CaseCategory.fetch_a_case_category(case_category_id)

        
    # New method to add a case category
    @staticmethod
    def add_case_category(name, description):
        return CaseCategory.add_case_category(name, description)
    
    
    # New method to update a case category
    @staticmethod
    def update_case_category(id, name, description):
        return CaseCategory.update_case_category(id, name, description)
    

    # New method to delete a case category
    @staticmethod
    def delete_case_category(id):
        return CaseCategory.delete_case_category(id)

