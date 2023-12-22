from app.db import mysql  

class CaseType:
    # method to fetch all case types
    @staticmethod
    def get_all_case_types():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM case_types")
        roles = cursor.fetchall()
        cursor.close()
        return roles
    
    # method to fetch a case type
    @staticmethod
    def get_case_type_by_id(case_type_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM case_types WHERE id = %s", (case_type_id,))
        case_type = cursor.fetchone()
        cursor.close()
        return case_type
    
    
    # method to add a case type
    @staticmethod
    def add_case_type(case_type):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO case_types (case_type) VALUES (%s)", (case_type,))
            mysql.connection.commit()
            cursor.close()
            return {'case_type': case_type}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a case type
    @staticmethod
    def update_case_type(case_type_id, new_case_type):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE case_types SET case_type = %s WHERE id = %s", (new_case_type, case_type_id))
            mysql.connection.commit()
            cursor.close()
            return {'case_type_id': case_type_id, 'case_type': new_case_type}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a case type    
    @staticmethod
    def delete_case_type(case_type_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM case_types WHERE id = %s", (case_type_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case_type_id': case_type_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


