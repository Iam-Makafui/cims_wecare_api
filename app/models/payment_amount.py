# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class PaymentAmount:
    # method for adding a payment amount detail
    @staticmethod
    def add_payment_amount(amount, currency):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO payment_amounts (amount, currency) VALUES (%s, %s)",
                (amount, currency,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'payment_amount': amount}
        except Exception as e:
            print(e)
            return None
        

    # method to fetch a payment amount
    @staticmethod
    def fetch_a_payment_amount(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    id, amount, currency
                FROM 
                    payment_amounts
                WHERE
                    id = %s
            """, (id,))
        payment_amount = cursor.fetchone()
        return payment_amount
        
        
    # method to fetch all payment amounts
    @staticmethod
    def get_all_payment_amounts():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM payment_amounts")
        payment_amounts = cursor.fetchall()
        cursor.close()
        connection.close()
        return payment_amounts
    
    # method to update a payment amount
    @staticmethod
    def update_payment_amount(id, amount, currency):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE payment_amounts
                SET amount = %s, currency = %s  
                WHERE id = %s
            """, (amount, currency, id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'updated_payment_amount': amount, 'currency': currency}
        except Exception as e:
            print(e)
            return None
        
        
    # method to delete a payment amount
    @staticmethod
    def delete_payment_amount(id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM payment_amounts 
                WHERE id = %s
            """, (id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'status': 'deleted'}
        except Exception as e:
            print(e)
            return None


