from flask import Blueprint, jsonify, request
from app.controllers.case_categories_controller import CaseCategoriesController
case_category_blueprint = Blueprint('case_category', __name__)

# route to fetch all case categories
@case_category_blueprint.route('/case_categories', methods=['GET'])
def get_all_case_caetegories():
    case_categories = CaseCategoriesController.get_all_case_caetegories()
    
    formatted_case_category = []
    for case_category in case_categories:
        formatted_case_category.append({
            'id': case_category[0],
            'name': case_category[1],
            'description': case_category[2],
            'created_at': case_category[3],
            'updated_at': case_category[4],
        })
    
    return jsonify({'case_categories': formatted_case_category, 'status_code': 200}), 200


# Route to fetch a case category by ID
@case_category_blueprint.route('/case_categories/<int:case_category_id>', methods=['GET'])
def get_case_category_by_id(case_category_id):
    case_category = CaseCategoriesController.get_case_category_by_id(case_category_id)
    if case_category:
        return jsonify({'case_category': case_category, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Case Category not found', 'status_code': 404}), 200


# New route to add a case category
@case_category_blueprint.route('/case_categories', methods=['POST'])
def add_case_type():
    required_fields = ['name', 'description']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    name = data['name']
    description = data['description']
    
    # Call controller method to add case category
    new_case_category = CaseCategoriesController.add_case_category(name, description)
    
    if new_case_category:
        return jsonify({'message': 'Case category added successfully', 'case_category': new_case_category, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add case category', 'status_code': 500}), 500
    
    
# New route to update a case category
@case_category_blueprint.route('/case_categories', methods=['PATCH'])
def update_case_category():
    required_fields = ['id', 'name', 'description']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    id = data['id']
    name = data['name']
    description = data['description']
    
    # Call controller method to update case category
    updated_case_category = CaseCategoriesController.update_case_category(id, name, description)

    if updated_case_category:
        return jsonify({'message': 'Case Category Updated Successfully', 'case_category': updated_case_category, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update case category', 'status_code': 500}), 200



# New route to delete a case category
@case_category_blueprint.route('/case_categories/<int:case_category_id>', methods=['DELETE'])
def delete_case_categoryby_id(case_category_id):
    deleted_case_category = CaseCategoriesController.delete_case_category(case_category_id)
    
    if deleted_case_category:
        return jsonify({'message': f'Case Category with ID {case_category_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete case category with ID {case_category_id}', 'status_code': 500}), 500
