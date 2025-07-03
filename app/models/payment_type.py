# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class PaymentType:
    # method for adding a payment type detail
    @staticmethod
    def add_payment_type(payment_type, description):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO payment_types (payment_type, description) VALUES (%s, %s)",
                (payment_type, description,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'payment_type': payment_type, 'description': description}
        except Exception as e:
            print(e)
            return None
        

    # method to fetch a payment type
    @staticmethod
    def fetch_a_payment_type(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    payment_type, description, inserted_at, updated_at
                FROM 
                    payment_types
                WHERE
                    id = %s
            """, (id,))
        payment_type = cursor.fetchone()
        return payment_type
        
        
    # method to fetch all payment types
    @staticmethod
    def get_all_payment_types():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM payment_types")
        payment_types = cursor.fetchall()
        cursor.close()
        connection.close()
        return payment_types
    
    # method to update a payment type
    @staticmethod
    def update_payment_type(id, payment_type, description):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE payment_types 
                SET payment_type = %s, description = %s, updated_at = NOW() 
                WHERE id = %s
            """, (payment_type, description, id))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'updated_payment_type': payment_type, 'description': description}
        except Exception as e:
            print(e)
            return None
        
        
    # method to delete a payment type
    @staticmethod
    def delete_payment_type(payment_type_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM payment_types 
                WHERE id = %s
            """, (payment_type_id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': payment_type_id, 'status': 'deleted'}
        except Exception as e:
            print(e)
            return None


