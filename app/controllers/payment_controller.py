from app.models.payment import Payment
import hashlib

class PaymentController:
    
    # New method to add payment types
    @staticmethod
    def add_single_payment(member_id, amount, payment_type_id, payment_method_id, payment_month, payment_year, payment_status, user_id, transaction_id):
        return Payment.add_single_payment(member_id, amount, payment_type_id, payment_method_id, payment_month, payment_year, payment_status, user_id, transaction_id)

     # New method to fetch all payments
    @staticmethod
    def get_all_payments():
        return Payment.get_all_payments()
    
    # New method to fetch a payment
    @staticmethod
    def fetch_a_payment(id):
        return Payment.fetch_a_payment(id)
    
    # New method to fetch all payments by status
    @staticmethod
    def fetch_all_payment_with_pending_status(payment_status):
        return Payment.fetch_all_payment_with_pending_status(payment_status)
    
    # New method to update a payment
    @staticmethod
    def update_payment_detail(member_id, amount_id, payment_method_id, payment_type_id, payment_month, payment_year, user_id, id):
        return Payment.update_payment_detail(member_id, amount_id, payment_method_id, payment_type_id, payment_month, payment_year, user_id, id)
    
    # New method to update a payment status
    @staticmethod
    def update_payment_status(id, payment_status):
        return Payment.update_payment_status(id, payment_status)
    
    
    # New method to delete a payment
    @staticmethod
    def delete_payment(payment_id):
        return Payment.delete_payment(payment_id)
    

    # New method to fetch last inserted payment
    @staticmethod
    def get_last_inserted_payment():
        return Payment.get_last_inserted_payment()