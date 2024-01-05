from app.db import mysql  

class Contribution:
    @staticmethod
    def get_all_case_contributions():
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    case_contributions.id, case_contributions.amount, case_contributions.inserted_at, case_contributions.updated_at, cases.title, members.member_id, members.name, users.firstname, users.lastname
                FROM 
                    case_contributions   
                INNER JOIN 
                    cases on case_contributions.case_id = cases.id
                INNER JOIN 
                    members on case_contributions.member_id = members.id
                INNER JOIN
                    users on case_contributions.user_id = users.id
                ORDER BY 
                    case_contributions.id DESC
            """)
            contributions = cursor.fetchall()
        return contributions
    
    # method to fetch a case contribution
    @staticmethod
    def get_a_case_contribution(contribution_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    case_contributions.id, case_contributions.amount, case_contributions.inserted_at, case_contributions.updated_at, cases.title, members.member_id, members.name, users.firstname, users.lastname
                FROM 
                    case_contributions   
                INNER JOIN 
                    cases on case_contributions.case_id = cases.id
                INNER JOIN 
                    members on case_contributions.member_id = members.id
                INNER JOIN
                    users on case_contributions.user_id = users.id
                WHERE 
                    case_contributions.id = %s 
                ORDER BY 
                    case_contributions.id DESC
            """, (contribution_id,))
            contributions = cursor.fetchone()
        return contributions
    
    
    # method to add a case contribution
    @staticmethod
    def add_case_contribution(case_id, member_id, amount, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO case_contributions (case_id, member_id, amount, user_id) VALUES (%s, %s, %s, %s)",
                           (case_id, member_id, amount, user_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case_id': case_id, 'member_id': member_id, 'amount': amount, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to update a case contribution
    @staticmethod
    def update_case_contribution(contribution_id, case_id, member_id, amount, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE case_contributions SET case_id = %s, member_id = %s, amount = %s, user_id = %s WHERE id = %s", 
                           (case_id, member_id, amount, user_id, contribution_id,))
            mysql.connection.commit()
            cursor.close()
            return {'case_id': case_id, 'member_id': member_id, 'amount': amount, 'user_id': user_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None
        
        
    # method to delete a case contribution    
    @staticmethod
    def delete_case_contriution(contribution_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM case_contributions WHERE id = %s", (contribution_id,))
            mysql.connection.commit()
            cursor.close()
            return {'contribution_id': contribution_id}
        except Exception as e:
            print(e)  # Handle the exception according to your application's error handling
            return None


