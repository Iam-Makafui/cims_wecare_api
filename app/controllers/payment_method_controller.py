from app.models.payment_method import PaymentMethod
import hashlib

class PaymentMethodController:
    
    # New method to add payment amount
    @staticmethod
    def add_payment_method(payment_method):
        return PaymentMethod.add_payment_method(payment_method)

    
    # New method to fetch all payment methods
    @staticmethod
    def get_all_payment_methods():
        return PaymentMethod.get_all_payment_methods()
    
    # New method to add a payment method
    @staticmethod
    def fetch_a_payment_method(id):
        return PaymentMethod.fetch_a_payment_method(id)
    
    # New method to update a payment method
    @staticmethod
    def update_payment_method(id, payment_method):
        return PaymentMethod.update_payment_method(id, payment_method)
    
    # New method to delete a payment method
    @staticmethod
    def delete_payment_method(id):
        return PaymentMethod.delete_payment_method(id)

    