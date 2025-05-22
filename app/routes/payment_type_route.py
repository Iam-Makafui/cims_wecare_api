from flask import Blueprint, jsonify, request
from app.controllers.payment_type_controller import PaymentTypeController

paymenttypes_blueprint = Blueprint('paymenttypes', __name__)

# route to fetch all paymenttypes
@paymenttypes_blueprint.route('/paymenttypes', methods=['GET'])
def get_all_payment_types():
    paymenttypes = PaymentTypeController.get_all_payment_types()
    
    formatted_paymenttypes = []
    for paymenttype in paymenttypes:
        formatted_paymenttypes.append({
            'id': paymenttype[0],
            'payment_type': paymenttype[1],
            'inserted_at': paymenttype[2],
            'updated_at': paymenttype[3]
        })
    
    return jsonify({'payment_types': formatted_paymenttypes})


# New route to add a payment type
@paymenttypes_blueprint.route('/paymenttypes', methods=['POST'])
def add_payment_type():
    required_fields = ['payment_type']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    payment_type = data['payment_type']

    # Call controller method to add payment type
    payment_type = PaymentTypeController.add_payment_type(payment_type)
    
    if payment_type:
        return jsonify({'message': 'Payment Type added successfully', 'payment_type': payment_type, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to Payment Type', 'status_code': 500}), 500
 
    
    
# New route to update a payment type detail
@paymenttypes_blueprint.route('/paymenttypes', methods=['PATCH'])
def update_payment_type():
    required_fields = ['id', 'payment_type']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['id']
    payment_type = data['payment_type']
    
    # Call controller method to update payment type detail
    update_payment_type = PaymentTypeController.update_payment_type(id, payment_type)
    
    if update_payment_type:
        return jsonify({'message': 'Payment Detail Updated Successfully', 'payment_type': update_payment_type, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update payment type', 'status_code': 500}), 500
    
    
# New route to delete a payment type
@paymenttypes_blueprint.route('/paymenttypes/<int:payment_type_id>', methods=['DELETE'])
def delete_payment_type(payment_type_id):
    delete_payment_type = PaymentTypeController.delete_payment_type(payment_type_id)
    
    if delete_payment_type:
        return jsonify({'message': f'Payment Type with ID {payment_type_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete payment type with ID {payment_type_id}', 'status_code': 500}), 500

# Route to fetch a specific payent id by ID
@paymenttypes_blueprint.route('/paymenttypes/<int:payment_type_id>', methods=['GET'])
def get_a_payment_type(payment_type_id):
    payment_type = PaymentTypeController.fetch_a_payment_type(payment_type_id)
    if payment_type:
        return jsonify({'payment_type': payment_type})
    else:
        return jsonify({'error': 'payment type not found', 'status_code': 404}), 200
   