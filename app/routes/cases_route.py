from flask import Blueprint, jsonify, request
from app.controllers.cases_controller import CasesController

case_blueprint = Blueprint('cases', __name__)


# New route to add a case
@case_blueprint.route('/cases', methods=['POST'])
def add_case():
    required_fields = ['case_id', 'title', 'description', 'beneficiary_id', 'category_id', 'issued_aid', 'case_status', 'processed_by']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    case_id = data['case_id']
    title = data['title']  
    description = data['description']
    beneficiary_id = data['beneficiary_id']
    category_id = data['category_id']
    issued_aid = data['issued_aid']
    case_status = data['case_status']
    processed_by = data['processed_by']
    
    # Call controller method to add a case
    add_case = CasesController.add_case(case_id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by)
    
    if add_case:
        return jsonify({'message': 'Case has been added successfully', 'data': add_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add case', 'status_code': 500}), 200
 

# route to fetch all cases
@case_blueprint.route('/cases', methods=['GET'])
def get_all_cases():
    cases = CasesController.get_all_cases()
    
    formatted_case = []
    for case in cases:
        formatted_case.append({
            'id': case[0],
            'case_id': case[1],
            'title': case[2],
            'description': case[3],
            'beneficiary_id': case[4],
            'category_id': case[5],
            'issued_aid': case[6],
            'case_status': case[7],
            'category_name': case[8],
            'category_description': case[9],
            'profile_id': case[10],
            'profile_first_name': case[11],
            'profile_last_name': case[12],
            'processed_by': case[13],
            'inserted_at': case[14],
            'updated_at': case[15],
            'member_image': case[16],
            'member_prefix': case[17],
            'member_first_name': case[18], 
            'member_last_name': case[19],
            'member_other_names': case[20],
            'member_identification_id': case[21],
            'member_primary_id': case[22]
        })
    
    return jsonify({'cases': formatted_case, 'status_code': 200}), 200



# route to fetch a case by ID
@case_blueprint.route('/cases/<int:case_id>', methods=['GET'])
def get_a_case(case_id):
    case = CasesController.get_case_by_id(case_id)
    
    if case:
        formatted_case = {
            'id': case[0],
            'case_id': case[1],
            'title': case[2],
            'description': case[3],
            'beneficiary_id': case[4],
            'category_id': case[5],
            'issued_aid': case[6],
            'case_status': case[7],
            'category_name': case[8],
            'category_description': case[9],
            'profile_id': case[10],
            'profile_first_name': case[11],
            'profile_last_name': case[12],
            'processed_by': case[13],
            'inserted_at': case[14],
            'updated_at': case[15],
            'member_image': case[16],
            'member_prefix': case[17],
            'member_first_name': case[18], 
            'member_last_name': case[19],
            'member_other_names': case[20],
            'member_identification_id': case[21]
        }
        
        return jsonify({'case': formatted_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Case not found', 'status_code': 404}), 404




# route to fetch all payments by cases
@case_blueprint.route('/cases/<string:case_status>', methods=['GET'])
def fetch_all_cases_by_status(case_status):
    cases = CasesController.fetch_all_cases_by_status(case_status)
    
    formatted_case = []
    for case in cases:
        formatted_case.append({
            'id': case[0],
            'case_id': case[1],
            'title': case[2],
            'description': case[3],
            'beneficiary_id': case[4],
            'category_id': case[5],
            'issued_aid': case[6],
            'case_status': case[7],
            'category_name': case[8],
            'category_description': case[9],
            'profile_id': case[10],
            'profile_first_name': case[11],
            'profile_last_name': case[12],
            'processed_by': case[13],
            'inserted_at': case[14],
            'updated_at': case[15],
            'member_image': case[16],
            'member_prefix': case[17],
            'member_first_name': case[18], 
            'member_last_name': case[19],
            'member_other_names': case[20],
            'member_identification_id': case[21],
            'member_primary_id': case[22]
        })
    
    return jsonify({'cases': formatted_case, 'status_code': 200}), 200


# New route to update a case 
@case_blueprint.route('/cases', methods=['PATCH'])
def update_case():
    required_fields = ['id', 'title', 'description', 'beneficiary_id', 'category_id', 'issued_aid', 'case_status', 'processed_by']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['id']
    title = data['title']
    description = data['description']
    beneficiary_id = data['beneficiary_id']
    category_id = data['category_id']
    issued_aid = data['issued_aid']
    case_status = data['case_status']
    processed_by = data['processed_by']
    
    
    # Call controller method to update case
    update_case = CasesController.update_case(id, title, description, beneficiary_id, category_id, issued_aid, case_status, processed_by)
    
    if update_case:
        return jsonify({'message': 'Case Updated Successfully', 'case': update_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update case', 'status_code': 500}), 500
    



# New route to update a case status
@case_blueprint.route('/cases/status', methods=['PATCH'])
def update_case_status():
    required_fields = ['case_id', 'case_status']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['case_id']
    case_status = data['case_status']
    
    # Call controller method to update case status
    update_case_status = CasesController.update_case_status(id, case_status)
    
    if update_case_status:
        return jsonify({'message': 'Case Status Updated Successfully', 'case_status': update_case_status, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update case status', 'status_code': 500}), 200
    
     
  
# New route to delete a case
@case_blueprint.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    
    delete_case = CasesController.delete_case(case_id)
    
    if delete_case:
        return jsonify({'message': f'Case with ID {case_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete case with ID {case_id}', 'status_code': 500}), 500
  

# Route to fetch last inserted case
@case_blueprint.route('/cases/recent', methods=['GET'])
def get_last_inserted_case():
    case = CasesController.get_last_inserted_case()
    if case:
        return jsonify({'case': {'id': case[0], 'case_id': case[1]}, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Cases table is empty', 'status_code': 404}), 200
