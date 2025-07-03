from flask import Blueprint, jsonify, request
from app.controllers.payment_method_controller import PaymentMethodController

paymentmethod_blueprint = Blueprint('paymentmethods', __name__)

# route to fetch all payment amounts
@paymentmethod_blueprint.route('/paymentmethods', methods=['GET'])
def get_all_payment_methods():
    paymentmethods = PaymentMethodController.get_all_payment_methods()
    
    formatted_paymentmethods = []
    for paymentmethod in paymentmethods:
        formatted_paymentmethods.append({
            'id': paymentmethod[0],
            'method_name': paymentmethod[1],
            'inserted_at': paymentmethod[2],
            'updated_at': paymentmethod[3],
            'description': paymentmethod[4]
        })
    
    return jsonify({'paymentmethods': formatted_paymentmethods})


# New route to add a payment methods
@paymentmethod_blueprint.route('/paymentmethods', methods=['POST'])
def add_payment_methods():
    required_fields = ['method_name', 'description']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    paymentmethod = data['method_name']
    description = data['description']
    
    # Call controller method to add payment method
    payment_method = PaymentMethodController.add_payment_method(paymentmethod, description)  

    if payment_method:
        return jsonify({'message': 'Payment Method added successfully', 'payment_method': payment_method, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to Payment Method', 'status_code': 500}), 500
 
    
    
# New route to update a payment methods
@paymentmethod_blueprint.route('/paymentmethods', methods=['PATCH'])
def update_payment_method():
    required_fields = ['id', 'method_name', 'description']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['id']
    payment_method = data['method_name']
    description = data['description']

    
    # Call controller method to update payment method detail
    update_paymentmethod = PaymentMethodController.update_payment_method(id, payment_method, description)
    
    if update_paymentmethod:
        return jsonify({'message': 'Payment Amount Updated Successfully', 'payment_method': update_paymentmethod, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update payment amount', 'status_code': 500}), 500
    
    
# New route to delete a payment method
@paymentmethod_blueprint.route('/paymentmethods/<int:payment_method_id>', methods=['DELETE'])
def delete_payment_method(payment_method_id):
    delete_payment_method = PaymentMethodController.delete_payment_method(payment_method_id)
    
    if delete_payment_method:
        return jsonify({'message': f'Payment Method with ID {payment_method_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete payment method with ID {payment_method_id}', 'status_code': 500}), 500



# Route to fetch a specific payment method by ID
@paymentmethod_blueprint.route('/paymentmethods/<int:payment_method_id>', methods=['GET'])
def get_a_payment_method(payment_method_id):
    payment_method = PaymentMethodController.fetch_a_payment_method(payment_method_id)

    if payment_method:
            return jsonify({'payment_method': {
                'id': payment_method[0],
                'payment_method': payment_method[1],
                'description': payment_method[2],
                'inserted_at': payment_method[3],
                'updated_at': payment_method[4]
           }, 'status_code': 200  }), 200
            
    else:
        return jsonify({'error': 'Payment method not found', 'status_code': 404}), 404