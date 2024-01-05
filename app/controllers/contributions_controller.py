from app.models.contributions import Contribution

class ContributionsController:
    # New method to fetch all case contributions
    @staticmethod
    def get_all_case_contributions():
        return Contribution.get_all_case_contributions()
    
    # New method to fetch a case contribution
    @staticmethod
    def get_case_contribution_by_id(contribution_id):
        return Contribution.get_a_case_contribution(contribution_id)

        
    # New method to add a case contribution
    @staticmethod
    def add_case_contribution(case_id, member_id, amount, user_id):
        return Contribution.add_case_contribution(case_id, member_id, amount, user_id)
    
    
    # New method to update a case contribution
    @staticmethod
    def update_case_contribution(contribution_id, case_id, member_id, amount, user_id):
        return Contribution.update_case_contribution(contribution_id, case_id, member_id, amount, user_id)
    
    
    # New method to delete a case contribution
    @staticmethod
    def delete_case_contriution(contribution_id):
        return Contribution.delete_case_contriution(contribution_id)

