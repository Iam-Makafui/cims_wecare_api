# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class Member:
    # method for adding a member detail
    @staticmethod
    def add_member(member_identification_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members (member_identification_id) VALUES (%s) RETURNING id",
                (member_identification_id,)
            )
            new_id = cursor.fetchone()[0]  # Get the auto-incremented ID
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'id': new_id, 'member_identification_id': member_identification_id}
        except Exception as e:
            print(e)
            return None
        
        
    # method for adding a member profile details
    @staticmethod
    def add_member_profile_details(member_id, member_image, prefix, first_name, last_name, other_names, gender, date_of_birth, place_of_birth, home_town, nationality, highest_level_of_education, institution_of_education, status_of_education, profession, employment_status, institution_of_employment, medical_conditions, mortality_status):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members_profile_detail (member_id, member_image, prefix, first_name, last_name, other_names, gender, date_of_birth, place_of_birth, home_town, nationality, highest_level_of_education, institution_of_education, status_of_education, profession, employment_status, institution_of_employment, medical_conditions, mortality_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (member_id, member_image, prefix, first_name, last_name, other_names,  gender, date_of_birth, place_of_birth, home_town, nationality, highest_level_of_education, institution_of_education, status_of_education, profession, employment_status, institution_of_employment, medical_conditions, mortality_status,))
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'member_id': member_id, 'member_image': member_image, 'prefix': prefix, 'first_name': first_name, 'last_name': last_name, 'other_names': other_names, 'gender': gender, 'date_of_birth': date_of_birth, 'place_of_birth': place_of_birth, 'home_town': home_town, 'nationality': nationality, 'highest_level_of_education': highest_level_of_education, 'institution_of_education': institution_of_education, 'status_of_education': status_of_education, 'profession': profession, 'employment_status': employment_status, 'institution_of_employment': institution_of_employment, 'medical_conditions': medical_conditions, 'mortality_status': mortality_status} 
        except Exception as e:
            print(e)
            return None


    # method for adding a member marriage and family details
    @staticmethod
    def add_member_family_and_marriage_details(member_id, marital_status, marriage_type, date_of_marriage, officiating_minister, place_of_marriage, marriage_license_number, fathers_name, fathers_phone_number, fathers_membership_status, fathers_mortality_status, mothers_name, mothers_phone_number, mothers_membership_status, mothers_mortality_status, spouse_name, spouse_phone, spouse_membership_status, spouse_mortality_status):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members_family_and_marriage_details (member_id, marital_status, marriage_type, date_of_marriage, officiating_minister, place_of_marriage, marriage_license_number, fathers_name, fathers_phone_number, fathers_membership_status, fathers_mortality_status, mothers_name, mothers_phone_number, mothers_membership_status, mothers_mortality_status, spouse_name, spouse_phone, spouse_membership_status, spouse_mortality_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (member_id, marital_status, marriage_type, date_of_marriage, officiating_minister, place_of_marriage,  marriage_license_number, fathers_name, fathers_phone_number, fathers_membership_status, fathers_mortality_status, mothers_name, mothers_phone_number, mothers_membership_status, mothers_mortality_status, spouse_name, spouse_phone, spouse_membership_status, spouse_mortality_status,))
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'member_id': member_id, 'marital_status': marital_status, 'marriage_type': marriage_type, 'date_of_marriage': date_of_marriage, 'officiating_minister': officiating_minister, 'place_of_marriage': place_of_marriage, 'marriage_license_number': marriage_license_number, 'fathers_name': fathers_name, 'fathers_phone_number': fathers_phone_number, 'fathers_membership_status': fathers_membership_status, 'fathers_mortality_status': fathers_mortality_status, 'mothers_name': mothers_name, 'mothers_phone_number': mothers_phone_number, 'mothers_membership_status': mothers_membership_status, 'mothers_mortality_status': mothers_mortality_status, 'spouse_name': spouse_name, 'spouse_phone': spouse_phone, 'spouse_membership_status': spouse_membership_status, 'spouse_mortality_status': spouse_mortality_status} 
        except Exception as e:
            print(e)
            return None
    
    
    
    # method for adding a member children detail
    @staticmethod
    def add_member_children_details(member_id, child_name, child_phone_number):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members_children_details (member_id, child_name, child_phone_number) VALUES (%s, %s, %s)",
                (member_id, child_name, child_phone_number,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'member_id': member_id, 'child_name': child_name, 'child_phone_number': child_phone_number}
        except Exception as e:
            print(e)
            return None
        
    
    
    
    # method for adding a member contact details
    @staticmethod
    def add_member_contact_details(member_id, phone_number, email, residential_address, postal_address, place_of_residence, closest_landmark):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members_contact_details (member_id, phone_number, email, residential_address, postal_address, place_of_residence, closest_landmark) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (member_id, phone_number, email, residential_address, postal_address, place_of_residence, closest_landmark,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'member_id': member_id, 'phone_number': phone_number, 'email': email, 'residential_address': residential_address, 'postal_address': postal_address, 'place_of_residence': place_of_residence, 'closest_landmark': closest_landmark}
        except Exception as e:
            print(e)
            return None
    
    
    # method for adding a member church details
    @staticmethod
    def add_member_church_details(member_id, department, areas_of_ministry, professional_service, member_status, water_baptism_date, place_of_baptism, officiating_minister, water_baptism_certificate_number, holy_spirit_baptism_status, member_since, transferred_from):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members_church_details (member_id, department, areas_of_ministry, professional_service, member_status, water_baptism_date, place_of_baptism, officiating_minister, water_baptism_certificate_number, holy_spirit_baptism_status, member_since, transferred_from) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (member_id, department, areas_of_ministry, professional_service, member_status, water_baptism_date, place_of_baptism, officiating_minister, water_baptism_certificate_number, holy_spirit_baptism_status, member_since, transferred_from,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'member_id': member_id, 'department': department, 'areas_of_ministry': areas_of_ministry, 'professional_service': professional_service, 'member_status': member_status, 'water_baptism_date': water_baptism_date, 'place_of_baptism': place_of_baptism, 'officiating_minister': officiating_minister, 'water_baptism_certificate_number': water_baptism_certificate_number, 'holy_spirit_baptism_status': holy_spirit_baptism_status, 'member_since': member_since, 'transferred_from': transferred_from}
        except Exception as e:
            print(e)
            return None
    
    # method for adding a member special note
    @staticmethod
    def add_member_special_note(member_id, special_note):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO members_special_notes (member_id, special_note) VALUES (%s, %s)",
                (member_id, special_note,)
            )
            new_id = cursor.fetchone()[0]  # Get the auto-incremented ID
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'id': new_id, 'member_id': member_id, 'special_note': special_note}
        except Exception as e:
            print(e)
            return None
    


    # method to fetch a user
    @staticmethod
    def get_last_inserted_member():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    members.id, members.member_identification_id
                FROM 
                    members
                ORDER BY 
                    members.id DESC LIMIT 1
            """)
        member = cursor.fetchone()
        return member
        
        


    # method to fetch all members
    @staticmethod
    def get_all_members():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    members.id,
                    members.member_identification_id, members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name, members_profile_detail.last_name, members_profile_detail.other_names,
                    members_profile_detail.gender, members_profile_detail.date_of_birth, members_profile_detail.place_of_birth, members_profile_detail.home_town, members_profile_detail.nationality, members_profile_detail.highest_level_of_education,
                    members_profile_detail.institution_of_education, members_profile_detail.status_of_education, members_profile_detail.profession, members_profile_detail.employment_status, members_profile_detail.institution_of_employment, members_profile_detail.medical_conditions, members_profile_detail.mortality_status,
                    members_family_and_marriage_details.marital_status, members_family_and_marriage_details.marriage_type, members_family_and_marriage_details.date_of_marriage, members_family_and_marriage_details.officiating_minister, members_family_and_marriage_details.place_of_marriage, members_family_and_marriage_details.marriage_license_number,
                    members_family_and_marriage_details.fathers_name, members_family_and_marriage_details.fathers_phone_number, members_family_and_marriage_details.fathers_membership_status, members_family_and_marriage_details.fathers_mortality_status,
                    members_family_and_marriage_details.mothers_name, members_family_and_marriage_details.mothers_phone_number, members_family_and_marriage_details.mothers_membership_status, members_family_and_marriage_details.mothers_mortality_status,
                    members_family_and_marriage_details.spouse_name, members_family_and_marriage_details.spouse_phone, members_family_and_marriage_details.spouse_membership_status, members_family_and_marriage_details.spouse_mortality_status,
                    members_children_details.child_name, members_children_details.child_phone_number,
                    members_contact_details.phone_number, members_contact_details.email, members_contact_details.residential_address, members_contact_details.postal_address, members_contact_details.place_of_residence, members_contact_details.closest_landmark,
                    members_church_details.department, members_church_details.areas_of_ministry, members_church_details.professional_service, members_church_details.member_status, members_church_details.water_baptism_date, members_church_details.place_of_baptism, members_church_details.officiating_minister, members_church_details.water_baptism_certificate_number,
                    members_church_details.holy_spirit_baptism_status, members_church_details.member_since, members_church_details.transferred_from,
                    members_special_notes.special_note, members.inserted_at, members.updated_at
                FROM 
                    members
                FULL OUTER JOIN members_profile_detail ON members.id = members_profile_detail.member_id
                FULL OUTER JOIN members_family_and_marriage_details ON members.id = members_family_and_marriage_details.member_id
                FULL OUTER JOIN members_children_details ON members.id = members_children_details.member_id
                FULL OUTER JOIN members_contact_details ON members.id = members_contact_details.member_id
                FULL OUTER JOIN members_church_details ON members.id = members_church_details.member_id
                FULL OUTER JOIN members_special_notes ON members.id = members_special_notes.member_id
                ORDER BY 
                    members.id DESC
            """)
        members = cursor.fetchall()
        return members



    # method to fetch a member
    @staticmethod
    def get_member_by_id(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    members.id,
                    members.member_identification_id, members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name, members_profile_detail.last_name, members_profile_detail.other_names,
                    members_profile_detail.gender, members_profile_detail.date_of_birth, members_profile_detail.place_of_birth, members_profile_detail.home_town, members_profile_detail.nationality, members_profile_detail.highest_level_of_education,
                    members_profile_detail.institution_of_education, members_profile_detail.status_of_education, members_profile_detail.profession, members_profile_detail.employment_status, members_profile_detail.institution_of_employment, members_profile_detail.medical_conditions, members_profile_detail.mortality_status,
                    members_family_and_marriage_details.marital_status, members_family_and_marriage_details.marriage_type, members_family_and_marriage_details.date_of_marriage, members_family_and_marriage_details.officiating_minister, members_family_and_marriage_details.place_of_marriage, members_family_and_marriage_details.marriage_license_number,
                    members_family_and_marriage_details.fathers_name, members_family_and_marriage_details.fathers_phone_number, members_family_and_marriage_details.fathers_membership_status, members_family_and_marriage_details.fathers_mortality_status,
                    members_family_and_marriage_details.mothers_name, members_family_and_marriage_details.mothers_phone_number, members_family_and_marriage_details.mothers_membership_status, members_family_and_marriage_details.mothers_mortality_status,
                    members_family_and_marriage_details.spouse_name, members_family_and_marriage_details.spouse_phone, members_family_and_marriage_details.spouse_membership_status, members_family_and_marriage_details.spouse_mortality_status,
                    members_children_details.child_name, members_children_details.child_phone_number,
                    members_contact_details.phone_number, members_contact_details.email, members_contact_details.residential_address, members_contact_details.postal_address, members_contact_details.place_of_residence, members_contact_details.closest_landmark,
                    members_church_details.department, members_church_details.areas_of_ministry, members_church_details.professional_service, members_church_details.member_status, members_church_details.water_baptism_date, members_church_details.place_of_baptism, members_church_details.officiating_minister, members_church_details.water_baptism_certificate_number,
                    members_church_details.holy_spirit_baptism_status, members_church_details.member_since, members_church_details.transferred_from,
                    members_special_notes.special_note, members.inserted_at, members.updated_at
                FROM 
                    members
                FULL OUTER JOIN members_profile_detail ON members.id = members_profile_detail.member_id
                FULL OUTER JOIN members_family_and_marriage_details ON members.id = members_family_and_marriage_details.member_id
                FULL OUTER JOIN members_children_details ON members.id = members_children_details.member_id
                FULL OUTER JOIN members_contact_details ON members.id = members_contact_details.member_id
                FULL OUTER JOIN members_church_details ON members.id = members_church_details.member_id
                FULL OUTER JOIN members_special_notes ON members.id = members_special_notes.member_id
                WHERE
                    members.id = %s
            """, (id,))
        member = cursor.fetchone()
        return member