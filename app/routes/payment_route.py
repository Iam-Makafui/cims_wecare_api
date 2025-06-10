from flask import Blueprint, jsonify, request
from app.controllers.payment_controller import PaymentController

payment_blueprint = Blueprint('payment', __name__)


# New route to add a single payment
@payment_blueprint.route('/payments', methods=['POST'])
def add_single_payment():
    required_fields = ['member_id', 'amount', 'payment_type_id', 'payment_method_id', 'payment_month', 'payment_year', 'payment_status', 'transaction_id', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    amount = data['amount']
    payment_type_id = data['payment_type_id']
    payment_method_id = data['payment_method_id']
    payment_month = data['payment_month']
    payment_year = data['payment_year']
    payment_status = data['payment_status']
    user_id = data['user_id']
    transaction_id = data['transaction_id']
    
    # Call controller method to add a single payment
    add_single_payment = PaymentController.add_single_payment(member_id, amount, payment_type_id, payment_method_id, payment_month, payment_year, payment_status, user_id, transaction_id)
    
    if add_single_payment:
        return jsonify({'message': 'Payment has been added successfully', 'data': add_single_payment, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add Payment', 'status_code': 500}), 500
 

# route to fetch all payments
@payment_blueprint.route('/payments', methods=['GET'])
def get_all_payments():
    payments = PaymentController.get_all_payments()
    
    formatted_payment = []
    for payment in payments:
        formatted_payment.append({
            'member_image': payment[0],
            'member_prefix': payment[1],
            'first_name': payment[2],
            'last_name': payment[3],
            'other_names': payment[4],
            'member_identification_id': payment[5],
            'member_id': payment[6],
            'amount': payment[7],
            'amount_id': payment[8],
            'currency': payment[9],
            'payment_method_id': payment[10],
            'payment_method_name': payment[11],
            'payment_status': payment[12],
            'payment_type_id': payment[13],
            'payment_type': payment[14],
            'payment_month': payment[15],
            'payment_year': payment[16],
            'profile_id': payment[17],
            'profile_first_name': payment[18],
            'profile_last_name': payment[19],
            'inserted_at': payment[20],
            'payment_id': payment[21],
            'profile_p_id': payment[22],
            'updated_at': payment[23],
            'transaction_id': payment[24]
        })
    
    return jsonify({'payments': formatted_payment})



# route to fetch a payment
@payment_blueprint.route('/payments/<int:payment_id>', methods=['GET'])
def get_a_payment(payment_id):
    payments = PaymentController.fetch_a_payment(payment_id)
    
    formatted_payments = []
    for payment in payments:
        formatted_payments.append({
            'member_image': payment[0],
            'member_prefix': payment[1],
            'first_name': payment[2],
            'last_name': payment[3],
            'other_names': payment[4],
            'member_identification_id': payment[5],
            'member_id': payment[6],
            'amount': payment[7],
            'amount_id': payment[8],
            'currency': payment[9],
            'payment_method_id': payment[10],
            'payment_method_name': payment[11],
            'payment_status': payment[12],
            'payment_type_id': payment[13],
            'payment_type': payment[14],
            'payment_month': payment[15],
            'payment_year': payment[16],
            'profile_id': payment[17],
            'profile_first_name': payment[18],
            'profile_last_name': payment[19],
            'inserted_at': payment[20],
            'payment_id': payment[21],
            'profile_p_id': payment[22],
            'updated_at': payment[23],
            'transaction_id': payment[24]
        })
    
    return jsonify({'payments': formatted_payments, 'status_code': 200}), 200



# route to fetch all payments by status
@payment_blueprint.route('/payments/<string:payment_status>', methods=['GET'])
def fetch_all_payment_with_pending_status(payment_status):
    payments = PaymentController.fetch_all_payment_with_pending_status(payment_status)
    
    formatted_payments = []
    for payment in payments:
        formatted_payments.append({
            'member_image': payment[0],
            'member_prefix': payment[1],
            'first_name': payment[2],
            'last_name': payment[3],
            'other_names': payment[4],
            'member_identification_id': payment[5],
            'member_id': payment[6],
            'amount': payment[7],
            'amount_id': payment[8],
            'currency': payment[9],
            'payment_method_id': payment[10],
            'payment_method_name': payment[11],
            'payment_status': payment[12],
            'payment_type_id': payment[13],
            'payment_type': payment[14],
            'payment_month': payment[15],
            'payment_year': payment[16],
            'profile_id': payment[17],
            'profile_first_name': payment[18],
            'profile_last_name': payment[19],
            'inserted_at': payment[20],
            'payment_id': payment[21],
            'profile_p_id': payment[22],
            'transaction_id': payment[23],
        })
    
    return jsonify({'payments': formatted_payments, 'status_code': 200}), 200


# New route to update a payment 
@payment_blueprint.route('/payments', methods=['PATCH'])
def update_payment():
    required_fields = ['member_id', 'amount_id', 'payment_method_id', 'payment_type_id', 'payment_month', 'payment_year', 'user_id', 'payment_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['payment_id']
    member_id = data['member_id']
    amount_id = data['amount_id']
    payment_method_id = data['payment_method_id']
    payment_type_id = data['payment_type_id']
    payment_month = data['payment_month']
    payment_year = data['payment_year']
    user_id = data['user_id']
    
    
    # Call controller method to update payment detail
    update_payment = PaymentController.update_payment_detail(member_id, amount_id, payment_method_id, payment_type_id, payment_month, payment_year, user_id, id)
    
    if update_payment:
        return jsonify({'message': 'Payment Updated Successfully', 'payment_method': update_payment, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update payment', 'status_code': 500}), 500
    



# New route to update a payment status
@payment_blueprint.route('/payments/status', methods=['PATCH'])
def update_payment_status():
    required_fields = ['payment_id', 'payment_status']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['payment_id']
    payment_status = data['payment_status']
    
    # Call controller method to update payment status
    update_payment_status = PaymentController.update_payment_status(id, payment_status)
    
    if update_payment_status:
        return jsonify({'message': 'Payment Status Updated Successfully', 'payment_status': update_payment_status, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update payment status', 'status_code': 500}), 500
    
     
  
# New route to delete a payment
@payment_blueprint.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    
    delete_payment = PaymentController.delete_payment(payment_id)
    
    if delete_payment:
        return jsonify({'message': f'Payment with ID {payment_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete payment with ID {payment_id}', 'status_code': 500}), 500
  

# Route to fetch last inserted payment
@payment_blueprint.route('/payments/recent', methods=['GET'])
def get_last_inserted_payment():
    payment = PaymentController.get_last_inserted_payment()
    if payment:
        return jsonify({'payment': {'id': payment[0], 'transaction_id': payment[1]}, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Payments table is empty', 'status_code': 404}), 200
