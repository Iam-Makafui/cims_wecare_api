from app.models.payment_amount import PaymentAmount
import hashlib

class PaymentAmountController:
    
    # New method to add payment amount
    @staticmethod
    def add_payment_amount(amount, currency):
        return PaymentAmount.add_payment_amount(amount, currency)

    
    # New method to fetch all payment amounts
    @staticmethod
    def get_all_payment_amounts():
        return PaymentAmount.get_all_payment_amounts()
    
    # New method to add a payment amount
    @staticmethod
    def fetch_a_payment_amount(id):
        return PaymentAmount.fetch_a_payment_amount(id)
    
    # New method to update a payment amount
    @staticmethod
    def update_payment_amount(id, amount, currency):
        return PaymentAmount.update_payment_amount(id, amount, currency)
    
    # New method to delete a payment amount
    @staticmethod
    def delete_payment_amount(id):
        return PaymentAmount.delete_payment_amount(id)

    