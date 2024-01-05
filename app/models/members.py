from app.db import mysql  

class Member:
    # method to fetch all members
    @staticmethod
    def get_all_members():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM members")
        roles = cursor.fetchall()
        cursor.close()
        return roles
    
    
    
    # method to fetch a member
    @staticmethod
    def get_member_by_id(member_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM members WHERE id = %s", (member_id,))
        role = cursor.fetchone()
        cursor.close()
        return role