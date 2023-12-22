from flask import Blueprint, jsonify, request
from app.controllers.case_types_controller import CaseTypesController
case_types_blueprint = Blueprint('case_type', __name__)

# route to fetch all case types
@case_types_blueprint.route('/case_types', methods=['GET'])
def get_case_types():
    case_types = CaseTypesController.get_all_case_types()
    
    formatted_case_types = []
    for case_type in case_types:
        formatted_case_types.append({
            'id': case_type[0],
            'case_type': case_type[1],
            'inserted_at': case_type[2],
            'updated_at': case_type[3]
        })
    
    return jsonify({'case_types': formatted_case_types})


# Route to fetch a specific case type by ID
@case_types_blueprint.route('/case_types/<int:case_type_id>', methods=['GET'])
def get_case_type_by_id(case_type_id):
    case_type = CaseTypesController.get_case_type_by_id(case_type_id)
    if case_type:
        return jsonify({'role': {'id': case_type[0], 'case_type': case_type[1], 'inserted_at': case_type[2], 'updated_at': case_type[3]} })
    else:
        return jsonify({'error': 'Case Type not found', 'status_code': 404}), 404


# New route to add a case type
@case_types_blueprint.route('/case_types', methods=['POST'])
def add_case_type():
    case_type = request.json.get('case_type')
    if not case_type:
        return jsonify({'error': 'Case type is required', 'status_code': 400}), 400
    
    # Call controller method to add case type
    new_case_type = CaseTypesController.add_case_type(case_type)
    
    if new_case_type:
        return jsonify({'message': 'Case type added successfully', 'case_type': new_case_type, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add case type', 'status_code': 500}), 500
    
    
# New route to update a case type  
@case_types_blueprint.route('/case_types/<int:case_type_id>', methods=['PATCH'])
def update_case_type_by_id(case_type_id):
    new_case_type = request.json.get('case_type')
    if not new_case_type:
        return jsonify({'error': 'New case type is required', 'status_code': 400}), 400

    updated_case = CaseTypesController.update_case_type(case_type_id, new_case_type)
    
    if updated_case:
        return jsonify({'message': f'Case Type with ID {case_type_id} updated successfully', 'case_type': updated_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to update case type with ID {case_type_id}', 'status_code': 500}), 500



# New route to delete a case type
@case_types_blueprint.route('/case_types/<int:case_type_id>', methods=['DELETE'])
def delete_case_type_by_id(case_type_id):
    deleted_case_type = CaseTypesController.delete_case_type(case_type_id)
    
    if deleted_case_type:
        return jsonify({'message': f'Case Type with ID {case_type_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete case type with ID {case_type_id}', 'status_code': 500}), 500
