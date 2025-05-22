# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class PaymentMethod:
    # method for adding a payment method detail
    @staticmethod
    def add_payment_method(payment_method):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO payment_methods (method_name) VALUES (%s)",
                (payment_method,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'payment_method': payment_method}
        except Exception as e:
            print(e)
            return None
        

    # method to fetch a payment method
    @staticmethod
    def fetch_a_payment_method(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    id, method_name
                FROM 
                    payment_methods
                WHERE
                    id = %s
            """, (id,))
        payment_method = cursor.fetchone()
        return payment_method
        
        
    # method to fetch all payment methods
    @staticmethod
    def get_all_payment_methods():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM payment_methods")
        payment_methods = cursor.fetchall()
        cursor.close()
        connection.close()
        return payment_methods
    
    # method to update a payment method
    @staticmethod
    def update_payment_method(id, payment_method):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE payment_methods
                SET method_name = %s  
                WHERE id = %s
            """, (payment_method, id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'updated_payment_method': payment_method}
        except Exception as e:
            print(e)
            return None
        
        
    # method to delete a payment method
    @staticmethod
    def delete_payment_method(id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM payment_methods 
                WHERE id = %s
            """, (id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'status': 'deleted'}
        except Exception as e:
            print(e)
            return None


