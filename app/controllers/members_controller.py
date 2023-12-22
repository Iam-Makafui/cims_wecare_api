from app.models.members import Member
import hashlib

class MembersController:
    # New method to fetch all members
    @staticmethod
    def get_all_members():
        return Member.get_all_members()
    
    
    # New method to fetch a member
    @staticmethod
    def get_member_by_id(member_id):
        return Member.get_member_by_id(member_id)