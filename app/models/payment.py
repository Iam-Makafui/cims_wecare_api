# from app.db import mysql  
from app.db import db  # Import the SQLAlchemy instance  


class Payment:
    # method for adding a single payment
    @staticmethod
    def add_single_payment(member_id, amount, payment_type_id, payment_method_id, payment_month, payment_year, payment_status, user_id, transaction_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO payments (member_id, amount_id, payment_method_id, payment_status, payment_type_id, payment_month, payment_year, processed_by, transaction_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (member_id, amount, payment_method_id, payment_status, payment_type_id, payment_month, payment_year, user_id, transaction_id,)
            )
            connection.commit()  # Commit changes to the database
            cursor.close()
            return {'member_id': member_id, 'amount': amount, 'payment_type_id': payment_type_id, 'payment_method_id': payment_method_id, payment_month: payment_month, 'payment_year': payment_year, 'payment_status': payment_status, 'user_id': user_id, 'transaction_id': transaction_id}
        except Exception as e:
            print(e)
            return None
        

    # method to fetch a payment
    @staticmethod
    def fetch_a_payment(id):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name, members_profile_detail.last_name, members_profile_detail.other_names,
                    members.member_identification_id, members.id AS memberId, payment_amounts.amount, payment_amounts.id AS amountId, payment_amounts.currency, payment_methods.id AS paymentMethodId, 
                    payment_methods.method_name, payments.payment_status, payment_types.id AS paymentTypeId, payment_types.payment_type, payments.month, payments.year, profiles.profile_id, profiles.first_name, profiles.last_name,
                    payments.inserted_at, payments.id, profiles.id AS profile_id, payments.updated_at, payments.transaction_id   
                FROM 
                    payments
                INNER JOIN
                    members_profile_detail ON payments.member_id = members_profile_detail.member_id
                INNER JOIN
                    members ON payments.member_id = members.id
                INNER JOIN
                    payment_amounts ON payments.amount_id = payment_amounts.id
                INNER JOIN
                    payment_methods ON payments.payment_method_id = payment_methods.id
                INNER JOIN
                    payment_types ON payments.payment_type_id = payment_types.id
                INNER JOIN
                    profiles ON payments.processed_by = profiles.id
                WHERE
                    payments.id = %s
            """, (id,))
        payment = cursor.fetchone()
        return payment
        
        
    # method to fetch all payment
    @staticmethod
    def get_all_payments():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name, members_profile_detail.last_name, members_profile_detail.other_names,
                    members.member_identification_id, members.id AS memberId, payment_amounts.amount, payment_amounts.id AS amountId, payment_amounts.currency, payment_methods.id AS paymentMethodId, 
                    payment_methods.method_name, payments.payment_status, payment_types.id AS paymentTypeId, payment_types.payment_type, payments.payment_month, payments.payment_year, profiles.profile_id, profiles.first_name AS profile_first_name, profiles.last_name AS profile_last_name, payments.inserted_at, payments.id, profiles.id, payments.updated_at,
                    payments.transaction_id 
                FROM 
                    payments
                INNER JOIN
                    members_profile_detail ON payments.member_id = members_profile_detail.member_id
                INNER JOIN
                    members ON payments.member_id = members.id
                INNER JOIN
                    payment_amounts ON payments.amount_id = payment_amounts.id
                INNER JOIN
                    payment_methods ON payments.payment_method_id = payment_methods.id
                INNER JOIN
                    payment_types ON payments.payment_type_id = payment_types.id
                INNER JOIN
                    profiles ON payments.processed_by = profiles.id
                ORDER BY
                    payments.id DESC
            """)
        payments = cursor.fetchall()
        cursor.close()
        connection.close()
        return payments



    # method to fetch all payments by status
    @staticmethod
    def fetch_all_payment_with_pending_status(payment_status):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    members_profile_detail.member_image, members_profile_detail.prefix, members_profile_detail.first_name, members_profile_detail.last_name, members_profile_detail.other_names,
                    members.member_identification_id, members.id AS memberId, payment_amounts.amount, payment_amounts.id AS amountId, payment_amounts.currency, payment_methods.id AS paymentMethodId, 
                    payment_methods.method_name, payments.payment_status, payment_types.id AS paymentTypeId, payment_types.payment_type, payments.payment_month, payments.payment_year, profiles.profile_id, profiles.first_name AS profile_first_name, profiles.last_name AS profile_last_name, payments.inserted_at, payments.id, profiles.id,
                    payments.transaction_id  
                FROM 
                    payments
                INNER JOIN
                    members_profile_detail ON payments.member_id = members_profile_detail.member_id
                INNER JOIN
                    members ON payments.member_id = members.id
                INNER JOIN
                    payment_amounts ON payments.amount_id = payment_amounts.id
                INNER JOIN
                    payment_methods ON payments.payment_method_id = payment_methods.id
                INNER JOIN
                    payment_types ON payments.payment_type_id = payment_types.id
                INNER JOIN
                    profiles ON payments.processed_by = profiles.id
                WHERE
                    payments.payment_status = %s
            """, (payment_status,))
        payment = cursor.fetchall()
        return payment
    
    # method to update a payment detail
    @staticmethod
    def update_payment_detail(member_id, amount_id, payment_method_id, payment_type_id, payment_month, payment_year, user_id, id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE payments 
                SET member_id = %s, amount_id = %s, payment_method_id = %s, payment_type_id = %s, payment_month = %s, payment_year = %s, processed_by = %s, updated_at = NOW()  
                WHERE id = %s
            """, (member_id, amount_id, payment_method_id, payment_type_id, payment_month, payment_year, user_id, id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'member_id': member_id, 'amount_id': amount_id, 'payment_method_id': payment_method_id, 'payment_type_id': payment_type_id, 'payment_month': payment_month, 'payment_year': payment_year, 'updated_by': user_id}
        except Exception as e:
            print(e)
            return None
        
        
    # method to update a payment status
    @staticmethod
    def update_payment_status(id, payment_status):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE payments 
                SET payment_status = %s, updated_at = NOW() 
                WHERE id = %s
            """, (payment_status, id))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': id, 'updated_payment_status': payment_status}
        except Exception as e:
            print(e)
            return None
        
        
    # method to delete a payment record
    @staticmethod
    def delete_payment(payment_id):
        try:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM payments
                WHERE id = %s
            """, (payment_id,))
            connection.commit()
            cursor.close()
            connection.close()
            return {'id': payment_id, 'status': 'deleted'}
        except Exception as e:
            print(e)
            return None
        
        
    # method to fetch last inserted payment
    @staticmethod
    def get_last_inserted_payment():
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT 
                    id, transaction_id
                FROM 
                    payments
                ORDER BY 
                    id DESC LIMIT 1
            """)
        member = cursor.fetchone()
        return member


