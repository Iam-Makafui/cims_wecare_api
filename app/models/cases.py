from app.db import mysql  

class Cases:
    # method to fetch all users
    @staticmethod
    def get_all_cases():
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    cases.id, case_types.case_type, cases.title, cases.description, members.member_id, members.name, cases.case_status, cases.issued_aid, users.firstname, users.lastname, cases.inserted_at, cases.updated_at
                FROM 
                    cases 
                INNER JOIN 
                    case_types on cases.case_type_id = case_types.id
                INNER JOIN 
                    members on cases.beneficiary_id = members.id
                INNER JOIN
                    users on cases.user_id = users.id
                ORDER BY 
                    cases.id DESC
            """)
            cases = cursor.fetchall()
        return cases
    
    
    # method to fetch a case
    @staticmethod
    def get_a_case(case_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    cases.id, case_types.case_type, cases.title, cases.description, members.member_id, members.name, cases.case_status, cases.issued_aid, users.firstname, users.lastname, cases.inserted_at, cases.updated_at
                FROM 
                    cases 
                INNER JOIN 
                    case_types on cases.case_type_id = case_types.id
                INNER JOIN 
                    members on cases.beneficiary_id = members.id
                INNER JOIN
                    users on cases.user_id = users.id
                WHERE 
                    cases.id = %s 
                ORDER BY 
                    cases.id DESC
            """, (case_id,))
            case = cursor.fetchone()
        return case
    
    
    # method to add a case
    @staticmethod
    def add_case(case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO cases (case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case_type_id': case_type_id, 'title': title, 'description': description, 'beneficiary_id': beneficiary_id, 'issued_aid': issued_aid, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a case
    @staticmethod
    def update_case(case_id, case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE cases SET case_type_id = %s, title = %s, description = %s, beneficiary_id = %s, case_status = %s, issued_aid = %s, user_id = %s WHERE id = %s", 
                           (case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id, case_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case_type_id': case_type_id, 'title': title, 'description': description, 'beneficiary_id': beneficiary_id, 'case_status': case_status, 'issued_aid': issued_aid, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
    # method to update a case issued aid details
    @staticmethod
    def update_case_issued_date(amount, cased_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE cases SET issued_aid = %s WHERE id = %s", 
                           (amount, cased_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case': "Issued Aid Updated"}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a case    
    @staticmethod
    def delete_case(case_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM cases WHERE id = %s", (case_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case_id': case_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


