from flask import Blueprint, jsonify, request
from app.controllers.payment_amount_controller import PaymentAmountController

paymentamount_blueprint = Blueprint('paymentamounts', __name__)

# route to fetch all payment amounts
@paymentamount_blueprint.route('/paymentamounts', methods=['GET'])
def get_all_payment_amounts():
    paymentamounts = PaymentAmountController.get_all_payment_amounts()
    
    formatted_paymentamounts = []
    for paymentamount in paymentamounts:
        formatted_paymentamounts.append({
            'id': paymentamount[0],
            'amount': paymentamount[1],
            'currency': paymentamount[2],
            'inserted_at': paymentamount[3],
            'updated_at': paymentamount[4]
        })
    
    return jsonify({'payment_amounts': formatted_paymentamounts})


# New route to add a payment amount
@paymentamount_blueprint.route('/paymentamounts', methods=['POST'])
def add_payment_amount():
    required_fields = ['amount', 'currency']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    amount = data['amount']
    currency = data['currency']

    # Call controller method to add payment amount
    payment_amount = PaymentAmountController.add_payment_amount(amount, currency)   

    if payment_amount:
        return jsonify({'message': 'Payment Amount added successfully', 'payment_amount': payment_amount, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to Payment Amount', 'status_code': 500}), 500
 
    
    
# New route to update a payment amount detail
@paymentamount_blueprint.route('/paymentamounts', methods=['PATCH'])
def update_payment_amount():
    required_fields = ['id', 'amount', 'currency']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['id']
    amount = data['amount']
    currency = data['currency']
    
    # Call controller method to update payment amount detail
    update_payment_amount = PaymentAmountController.update_payment_amount(id, amount, currency)
    
    if update_payment_amount:
        return jsonify({'message': 'Payment Amount Updated Successfully', 'payment_amount': update_payment_amount, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update payment amount', 'status_code': 500}), 500
    
    
# New route to delete a payment amount
@paymentamount_blueprint.route('/paymentamounts/<int:payment_amount_id>', methods=['DELETE'])
def delete_payment_amount(payment_amount_id):
    delete_payment_amount = PaymentAmountController.delete_payment_amount(payment_amount_id)
    
    if delete_payment_amount:
        return jsonify({'message': f'Payment Amount with ID {payment_amount_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete payment amount with ID {payment_amount_id}', 'status_code': 500}), 500

# Route to fetch a specific payment amount by ID
@paymentamount_blueprint.route('/paymentamounts/<int:payment_amount_id>', methods=['GET'])
def get_a_payment_type(payment_amount_id):
    payment_amount = PaymentAmountController.fetch_a_payment_amount(payment_amount_id)

    if payment_amount:
            return jsonify({'payment_amount': {
                'id': payment_amount[0],
                'amount': payment_amount[1],
                'currency': payment_amount[2],
                'inserted_at': payment_amount[3],
                'updated_at': payment_amount[4]
           }, 'status_code': 200  }), 200
            
    else:
        return jsonify({'error': 'Payment amount not found', 'status_code': 404}), 404