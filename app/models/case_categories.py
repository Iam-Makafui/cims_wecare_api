# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class CaseCategory:
    # method for adding a case category detail
    @staticmethod
    def add_case_category(name, description):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO case_categories (name, description) VALUES (%s, %s)",
                (name, description,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'case_category_name': name, 'description': description}
        except Exception as e:
            print(e)
            return None
        

    # method to fetch a case category
    @staticmethod
    def fetch_a_case_category(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    *
                FROM 
                    case_categories
                WHERE
                    id = %s
            """, (id,))
        case_category = cursor.fetchone()
        return case_category
        
        
    # method to fetch all case categories
    @staticmethod
    def get_all_case_caetegories():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM case_categories ORDER BY created_at DESC")
        case_categories = cursor.fetchall()
        cursor.close()
        connection.close()
        return case_categories
    
    # method to update a case category
    @staticmethod
    def update_case_category(id, name, description):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE case_categories 
                SET name = %s, description = %s 
                WHERE id = %s
            """, (name, description, id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'name': name, 'description': description}
        except Exception as e:
            print(e)
            return None
        
        
    # method to delete a case category
    @staticmethod
    def delete_case_category(id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM case_categories 
                WHERE id = %s
            """, (id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'status': 'deleted'}
        except Exception as e:
            print(e)
            return None


