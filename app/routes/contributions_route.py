from flask import Blueprint, jsonify, request
from app.controllers.contributions_controller import ContributionsController

contributions_blueprint = Blueprint('contributions', __name__)

# route to fetch all cases
@contributions_blueprint.route('/contributions', methods=['GET'])
def get_cases():
    contributions = ContributionsController.get_all_case_contributions()
    
    formatted_contributions = []
    for contribution in contributions:
        formatted_contributions.append({
            'id': contribution[0],
            'amount': contribution[1],
            'inserted_at': contribution[2],
            'updated_at': contribution[3],
            'case_title': contribution[4],
            'member_id': contribution[5],
            'member_name': contribution[6],
            'firstname': contribution[7],
            'lastname': contribution[8]
        })
    
    return jsonify({'cases': formatted_contributions})


# Route to fetch a specific case contribution by ID
@contributions_blueprint.route('/contributions/<int:contribution_id>', methods=['GET'])
def get_case_contribution_by_id(contribution_id):
    case_contribution = ContributionsController.get_case_contribution_by_id(contribution_id)
    if case_contribution:
        return jsonify({'case': {'id': case_contribution[0], 'amount': case_contribution[1], 'inserted_at': case_contribution[2], 'updated_at': case_contribution[3], 'title': case_contribution[4], 'member_id': case_contribution[5], 'member_name': case_contribution[6], 'firstname': case_contribution[7], 'lastname': case_contribution[8]} })
    else:
        return jsonify({'error': 'Case Contribution not found', 'status_code': 404}), 404


# New route to add a case
@contributions_blueprint.route('/contributions', methods=['POST'])
def add_case_contribution():
    required_fields = ['case_id', 'member_id', 'amount', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    case_id = data['case_id']
    member_id = data['member_id']
    amount = data['amount']
    user_id = data['user_id']

    # Call controller method to add case contribution
    new_case_contribution = ContributionsController.add_case_contribution(case_id, member_id, amount, user_id)
    
    if new_case_contribution:
        return jsonify({'message': 'Case Contribtution added successfully', 'case_contribution': new_case_contribution, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add case contribution', 'status_code': 500}), 500
    
    
# New route to update a case contribution
@contributions_blueprint.route('/contributions', methods=['PATCH'])
def update_case_contribution():
    required_fields = ['contribution_id', 'case_id', 'member_id', 'amount', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    contribution_id = data['contribution_id']
    case_id = data['case_id']
    member_id = data['member_id']
    amount = data['amount']
    user_id = data['user_id']    

    # Call controller method to update case contribution
    update_case_contribution = ContributionsController.update_case_contribution(contribution_id, case_id, member_id, amount, user_id)
    
    if update_case_contribution:
        return jsonify({'message': 'Case Contribution Updated Successfully', 'case': update_case_contribution, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update case', 'status_code': 500}), 500
    

# New route to delete a case contribution
@contributions_blueprint.route('/contributions/<int:contribution_id>', methods=['DELETE'])
def delete_case_contribution_by_id(contribution_id):
    deleted_case_contribution = ContributionsController.delete_case_contriution(contribution_id)
    
    if deleted_case_contribution:
        return jsonify({'message': f'Case Contribution with ID {contribution_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete case contribution with ID {contribution_id}', 'status_code': 500}), 500
