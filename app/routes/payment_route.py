from flask import Blueprint, jsonify, request
from app.controllers.payment_controller import PaymentController

payment_blueprint = Blueprint('payment', __name__)


# New route to add a single payment
@payment_blueprint.route('/payment/single_payemnt', methods=['POST'])
def add_single_payment():
    required_fields = ['member_id, amount, payment_type_id, payment_method_id, payment_month, payment_year, payment_status, user_id']
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
    
    # Call controller method to add a single payment
    add_single_payment = PaymentController.add_single_payment(member_id, amount, payment_type_id, payment_method_id, payment_month, payment_year, payment_status, user_id)
    
    if add_single_payment:
        return jsonify({'message': 'Payment has been added successfully', 'member_id': amount, 'payment_type_id': payment_type_id, 'payment_method_id': payment_method_id, 'payment_month': payment_month, 'payment_year': payment_year, 'payment_status': payment_status, 'user_id': user_id,  'status_code': 200}), 200
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
            'payment_method_id': payment[11],
            'method_name': payment[12],
            'payment_status': payment[13],
            'payment_type_id': payment[14],
            'payment_type': payment[15],
            'month': payment[16],
            'year': payment[17],
            'profile_id': payment[18],
            'first_name': payment[19],
            'last_name': payment[20],
            'inserted_at': payment[21]
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
            'payment_method_id': payment[11],
            'method_name': payment[12],
            'payment_status': payment[13],
            'payment_type_id': payment[14],
            'payment_type': payment[15],
            'month': payment[16],
            'year': payment[17],
            'profile_id': payment[18],
            'first_name': payment[19],
            'last_name': payment[20],
            'inserted_at': payment[21]
        })
    
    return jsonify({'payments': formatted_payments, 'status_code': 200}), 200



# New route to update a payment 
@payment_blueprint.route('/payments', methods=['PATCH'])
def update_payment():
    required_fields = ['member_id', 'amount_id', 'payment_method_id', 'payment_type_id', 'payment_month', 'payment_year', 'id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['id']
    member_id = data['member_id']
    amount_id = data['amount_id']
    payment_method_id = data['payment_method_id']
    payment_type_id = data['payment_type_id']
    payment_month = data['payment_month']
    payment_year = data['payment_year']
    
    
    # Call controller method to update payment detail
    update_payment = PaymentController.update_payment_detail(member_id, amount_id, payment_method_id, payment_type_id, payment_month, payment_year, id)
    
    if update_payment:
        return jsonify({'message': 'Payment Updated Successfully', 'payment_method': update_payment, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update payment', 'status_code': 500}), 500
    



# New route to update a payment status
@payment_blueprint.route('/payments', methods=['PATCH'])
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
  

