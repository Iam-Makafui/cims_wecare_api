from flask import Blueprint, jsonify, request
from app.controllers.cases_controller import CasesController

cases_blueprint = Blueprint('cases', __name__)

# route to fetch all cases
@cases_blueprint.route('/cases', methods=['GET'])
def get_cases():
    cases = CasesController.get_all_cases()
    
    formatted_cases = []
    for case in cases:
        formatted_cases.append({
            'id': case[0],
            'case_type': case[1],
            'title': case[2],
            'description': case[3],
            'member_id': case[4],
            'name': case[5],
            'case_status': case[6],
            'issued_aid': case[7],
            'firstname': case[8],
            'lastname': case[9],
            'inserted_at': case[10],
            'updated_at': case[11]
        })
    
    return jsonify({'cases': formatted_cases})


# Route to fetch a specific case by ID
@cases_blueprint.route('/cases/<int:case_id>', methods=['GET'])
def get_case_by_id(case_id):
    case = CasesController.get_case_by_id(case_id)
    if case:
        return jsonify({'case': {'id': case[0], 'case_type': case[1], 'title': case[2], 'description': case[3], 'member_id': case[4], 'name': case[5], 'case_status': case[6], 'issued_aid': case[7], 'firstname': case[8], 'lastname': case[9], 'inserted_at': case[10], 'updated_at': case[11]} })
    else:
        return jsonify({'error': 'Case not found', 'status_code': 404}), 404


# New route to add a case
@cases_blueprint.route('/cases', methods=['POST'])
def add_case():
    required_fields = ['case_type_id', 'title', 'description', 'beneficiary_id', 'case_status', 'issued_aid', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    case_type_id = data['case_type_id']
    title = data['title']
    description = data['description']
    beneficiary_id = data['beneficiary_id']
    case_status = data['case_status']
    issued_aid = data['issued_aid']
    user_id = data['user_id']

    # Call controller method to add case
    new_case = CasesController.add_case(case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id)
    
    if new_case:
        return jsonify({'message': 'Case added successfully', 'case': new_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add case', 'status_code': 500}), 500
    
    
# New route to update a case
@cases_blueprint.route('/cases', methods=['PATCH'])
def update_case():
    required_fields = ['case_id', 'case_type_id', 'title', 'description', 'beneficiary_id', 'case_status', 'issued_aid', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    case_type_id = data['case_type_id']
    title = data['title']
    description = data['description']
    beneficiary_id = data['beneficiary_id']
    case_status = data['case_status']
    issued_aid = data['issued_aid']
    user_id = data['user_id']
    case_id = data['case_id']
    

    # Call controller method to update case
    update_case = CasesController.update_case(case_id, case_type_id, title, description, beneficiary_id, case_status, issued_aid, user_id)
    
    if update_case:
        return jsonify({'message': 'Case Updated Successfully', 'case': update_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update case', 'status_code': 500}), 500
    


# New route to update an issued aid
@cases_blueprint.route('/cases/issued_aid', methods=['PATCH'])
def update_issued_aid():
    required_fields = ['amount', 'case_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    amount = data['amount']
    case_id = data['case_id']

    # Call controller method to update case issued aid
    update_issued_aid = CasesController.update_case_issued_aid(amount, case_id)
    
    if update_issued_aid:
        return jsonify({'message': 'Case Issued Aid Updated Successfully', 'case': update_issued_aid, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update issued aid', 'status_code': 500}), 500



# New route to delete a role
@cases_blueprint.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case_by_id(case_id):
    deleted_case = CasesController.delete_case(case_id)
    
    if deleted_case:
        return jsonify({'message': f'Case with ID {case_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete case with ID {case_id}', 'status_code': 500}), 500
