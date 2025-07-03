from app.models.payment_type import PaymentType
import hashlib

class PaymentTypeController:
    
    # New method to add payment types
    @staticmethod
    def add_payment_type(payment_type, description):
        return PaymentType.add_payment_type(payment_type, description)

    
    # New method to fetch all payment types
    @staticmethod
    def get_all_payment_types():
        return PaymentType.get_all_payment_types()
    
    # New method to add a payment type
    @staticmethod
    def fetch_a_payment_type(id):
        return PaymentType.fetch_a_payment_type(id)
    
    # New method to update a payment type
    @staticmethod
    def update_payment_type(id, payment_type, description):
        return PaymentType.update_payment_type(id, payment_type, description)
    
    # New method to delete a payment type
    @staticmethod
    def delete_payment_type(payment_type_id):
        return PaymentType.delete_payment_type(payment_type_id)

    