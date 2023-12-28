from flask import Blueprint, jsonify, request
from app.controllers.dues_controller import DuesController

dues_blueprint = Blueprint('dues', __name__)

# route to fetch all dues
@dues_blueprint.route('/dues', methods=['GET'])
def get_dues():
    dues = DuesController.get_all_dues()
    
    formatted_dues = []
    for due in dues:
        formatted_dues.append({
            'member_id': due[0],
            'name': due[1],
            'id': due[2],
            'amount': due[3],
            'approval_status': due[4],
            'payment_method': due[5],
            'month_and_year': due[6],
            'inserted_at': due[7],
            'firstname': due[8],
            'lastname': due[9]
        })
    
    return jsonify({'dues': formatted_dues})


# Route to fetch a specific due by ID
@dues_blueprint.route('/dues/<int:due_id>', methods=['GET'])
def get_due_by_id(due_id):
    due = DuesController.get_due_by_id(due_id)
    if due:
        return jsonify({'due': {'member_id': due[0], 'name': due[1], 'id': due[2], 'amount': due[3], 'approval_status': due[4], 'payment_method': due[5], 'month_and_year': due[6], 'inserted_at': due[7], 'firstname': due[8], 'lastname': due[9]} })
    else:
        return jsonify({'error': 'Due not found', 'status_code': 404}), 404


# New route to add a due
@dues_blueprint.route('/dues', methods=['POST'])
def add_due():
    required_fields = ['member_id', 'amount', 'approval_status', 'payment_method', 'month_and_year', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    member_id = data['member_id']
    amount = data['amount']
    approval_status = data['approval_status']
    payment_method = data['payment_method']
    month_and_year = data['month_and_year']
    user_id = data['user_id']

    # Call controller method to add due
    new_due = DuesController.add_due(member_id, amount, approval_status, payment_method, month_and_year, user_id)
    
    if new_due:
        return jsonify({'message': 'Due added successfully', 'due': new_due, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add case', 'status_code': 500}), 500
    
    
# New route to update a due
@dues_blueprint.route('/dues', methods=['PATCH'])
def update_due():
    required_fields = ['due_id', 'member_id', 'amount', 'payment_method', 'month_and_year', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    due_id = data['due_id']
    member_id = data['member_id']
    amount = data['amount']
    payment_method = data['payment_method']
    month_and_year = data['month_and_year']
    user_id = data['user_id']
    

    # Call controller method to update due
    update_due = DuesController.update_due(due_id, member_id, amount, payment_method, month_and_year, user_id)
    
    if update_due:
        return jsonify({'message': 'Due Updated Successfully', 'due': update_due, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update due', 'status_code': 500}), 500
    


# New route to update due approval status
@dues_blueprint.route('/dues/approval_status', methods=['PATCH'])
def update_due_approval_status():
    required_fields = ['approval_status', 'due_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    approval_status = data['approval_status']
    due_id = data['due_id']

    # Call controller method to update due approval status
    update_approval_status = DuesController.update_due_approval_status(approval_status, due_id)
    
    if update_approval_status:
        return jsonify({'message': 'Approval Status Updated Successfully', 'due': update_approval_status, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update approval status', 'status_code': 500}), 500



# New route to delete a due
@dues_blueprint.route('/dues/<int:due_id>', methods=['DELETE'])
def delete_due_by_id(due_id):
    deleted_due = DuesController.delete_due(due_id)
    
    if deleted_due:
        return jsonify({'message': f'Due with ID {due_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete due with ID {due_id}', 'status_code': 500}), 500
