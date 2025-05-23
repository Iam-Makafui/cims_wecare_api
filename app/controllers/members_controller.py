from app.models.members import Member
import hashlib

class MembersController:
    # method for adding a member detail
    @staticmethod
    def add_member(member_identification_id):
        return Member.add_member(member_identification_id)


    # method for adding a member profile details
    @staticmethod
    def add_member_profile_details(member_id, member_image, prefix, first_name, last_name, other_names, gender, date_of_birth, place_of_birth, home_town, nationality, highest_level_of_education, institution_of_education, status_of_education, profession, employment_status, institution_of_employment, medical_conditions, mortality_status):
        return Member.add_member_profile_details(member_id, member_image, prefix, first_name, last_name, other_names, gender, date_of_birth, place_of_birth, home_town, nationality, highest_level_of_education, institution_of_education, status_of_education, profession, employment_status, institution_of_employment, medical_conditions, mortality_status)


    # method for adding a member marriage and family details
    @staticmethod
    def add_member_family_and_marriage_details(member_id, marital_status, marriage_type, date_of_marriage, officiating_minister, place_of_marriage, marriage_license_number, fathers_name, fathers_phone_number, fathers_membership_status, fathers_mortality_status, mothers_name, mothers_phone_number, mothers_membership_status, mothers_mortality_status, spouse_name, spouse_phone, spouse_membership_status, spouse_mortality_status):
        return Member.add_member_family_and_marriage_details(member_id, marital_status, marriage_type, date_of_marriage, officiating_minister, place_of_marriage, marriage_license_number, fathers_name, fathers_phone_number, fathers_membership_status, fathers_mortality_status, mothers_name, mothers_phone_number, mothers_membership_status, mothers_mortality_status, spouse_name, spouse_phone, spouse_membership_status, spouse_mortality_status)


    # method for adding a member children detail
    @staticmethod
    def add_member_children_details(member_id, child_name, child_phone_number):
        return Member.add_member_children_details(member_id, child_name, child_phone_number)


    # method for adding a member contact details
    @staticmethod
    def add_member_contact_details(member_id, phone_number, email, residential_address, postal_address, place_of_residence, closest_landmark):
        return Member.add_member_contact_details(member_id, phone_number, email, residential_address, postal_address, place_of_residence, closest_landmark)

    # method for adding a member church details
    @staticmethod
    def add_member_church_details(member_id, department, areas_of_ministry, professional_service, member_status, water_baptism_date, place_of_baptism, officiating_minister, water_baptism_certificate_number, holy_spirit_baptism_status, member_since, transferred_from):
        return Member.add_member_church_details(member_id, department, areas_of_ministry, professional_service, member_status, water_baptism_date, place_of_baptism, officiating_minister, water_baptism_certificate_number, holy_spirit_baptism_status, member_since, transferred_from)


    # method for adding a member detail
    @staticmethod
    def add_member_special_note(member_id, special_note):
        return Member.add_member_special_note(member_id, special_note)



    # New method to fetch last inserted member
    @staticmethod
    def get_last_inserted_member():
        return Member.get_last_inserted_member()
    
    
    # New method to fetch all members
    @staticmethod
    def get_all_members():
        return Member.get_all_members()
    
    
    # New method to fetch a member
    @staticmethod
    def get_member_by_id(member_id):
        return Member.get_member_by_id(member_id)