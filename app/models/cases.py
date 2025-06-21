# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class Case:
    # method for adding a case
    @staticmethod
    def add_case(case_id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO cases (case_id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (case_id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'case_id': case_id, 'title': title, 'description': description, 'beneficiary_id': beneficiary_id, 'category_id': category_id, 'issued_aid': issued_aid, 'case_status': case_status, 'processed_by': processed_by}
        except Exception as e:
            print(e)
            return None
        

    # method to fetch a case
    @staticmethod
    def fetch_a_case(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    cases.id, cases.case_id, cases.title, cases.description, cases.beneficiary_id, cases.category_id, cases.issued_aid, cases.case_status, 
                    case_categories.name AS category_name, case_categories.description AS category_description, profiles.profile_id, profiles.first_name AS profile_first_name, 
                    profiles.last_name AS profile_last_name, cases.processed_by, cases.created_at, cases.updated_at,
                    members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name AS member_first_name,
                    members_profile_detail.last_name AS member_last_name, members_profile_detail.other_names AS member_other_names, members.member_identification_id
                FROM 
                    cases
                INNER JOIN
                    case_categories ON cases.category_id = case_categories.id
                INNER JOIN
                    profiles ON cases.processed_by = profiles.id
                INNER JOIN
                    members ON cases.beneficiary_id = members.id
                INNER JOIN
                    members_profile_detail ON cases.beneficiary_id = members_profile_detail.member_id
                WHERE
                    cases.id = %s
            """, (id,))
        case = cursor.fetchone()
        return case
        
        
    # method to fetch all cases
    @staticmethod
    def get_all_cases():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    cases.id, cases.case_id, cases.title, cases.description, cases.beneficiary_id, cases.category_id, cases.issued_aid, cases.case_status, 
                    case_categories.name AS category_name, case_categories.description AS category_description, profiles.profile_id, profiles.first_name AS profile_first_name, 
                    profiles.last_name AS profile_last_name, cases.processed_by, cases.created_at, cases.updated_at,
                    members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name AS member_first_name,
                    members_profile_detail.last_name AS member_last_name, members_profile_detail.other_names AS member_other_names, members.member_identification_id, members.id AS member_primary_id
                FROM 
                    cases
                INNER JOIN
                    case_categories ON cases.category_id = case_categories.id
                INNER JOIN
                    profiles ON cases.processed_by = profiles.id
                INNER JOIN
                    members ON cases.beneficiary_id = members.id
                INNER JOIN
                    members_profile_detail ON cases.beneficiary_id = members_profile_detail.member_id
                ORDER BY
                    cases.id DESC
            """)
        cases = cursor.fetchall()
        cursor.close()
        connection.close()
        return cases



    # method to fetch all cases by status
    @staticmethod
    def fetch_all_cases_by_status(case_status):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    cases.id, cases.case_id, cases.title, cases.description, cases.beneficiary_id, cases.category_id, cases.issued_aid, cases.case_status, 
                    case_categories.name AS category_name, case_categories.description AS category_description, profiles.profile_id, profiles.first_name AS profile_first_name, 
                    profiles.last_name AS profile_last_name, cases.processed_by, cases.created_at, cases.updated_at,
                    members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name AS member_first_name,
                    members_profile_detail.last_name AS member_last_name, members_profile_detail.other_names AS member_other_names, members.member_identification_id, members.id AS member_primary_id
                FROM 
                    cases
                INNER JOIN
                    case_categories ON cases.category_id = case_categories.id
                INNER JOIN
                    profiles ON cases.processed_by = profiles.id
                INNER JOIN
                    members ON cases.beneficiary_id = members.id
                INNER JOIN
                    members_profile_detail ON cases.beneficiary_id = members_profile_detail.member_id
                WHERE
                    cases.case_status = %s
            """, (case_status,))
        cases = cursor.fetchall()
        return cases
    
    # method to update a case
    @staticmethod
    def update_case(id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE cases
                SET title = %s, description = %s, beneficiary_id = %s, category_id = %s, issued_aid = %s, case_status = %s, processed_by = %s, updated_at = NOW() 
                WHERE id = %s
            """, ( title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by, id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'title': title, 'description': description, 'beneficiary_id': beneficiary_id, 'category_id': category_id, 'issued_aid': issued_aid, 'case_status': case_status, 'processed_by': processed_by}
        except Exception as e:
            print(e)
            return None
        
        
    # method to update a case status
    @staticmethod
    def update_case_status(id, case_status):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE cases 
                SET case_status = %s, updated_at = NOW() 
                WHERE id = %s
            """, (case_status, id))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'updated_case_status': case_status}
        except Exception as e:
            print(e)
            return None
        
        
    # method to delete a case
    @staticmethod
    def delete_case(id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM cases
                WHERE id = %s
            """, (id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'status': 'deleted'}
        except Exception as e:
            print(e)
            return None
        
        
    # method to fetch last inserted case
    @staticmethod
    def get_last_inserted_case():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    id, case_id
                FROM 
                    cases
                ORDER BY 
                    id DESC LIMIT 1
            """)
        case = cursor.fetchone()
        return case


