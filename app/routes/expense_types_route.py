from flask import Blueprint, jsonify, request
from app.controllers.expense_types_controller import ExpenseTypesController
expense_types_blueprint = Blueprint('expense_type', __name__)

# route to fetch all expense types
@expense_types_blueprint.route('/expense_types', methods=['GET'])
def get_expense_types():
    expense_types = ExpenseTypesController.get_all_expense_types()
    
    formatted_expense_types = []
    for expense_type in expense_types:
        formatted_expense_types.append({
            'id': expense_type[0],
            'expense_type': expense_type[1],
            'inserted_at': expense_type[2],
            'updated_at': expense_type[3]
        })
    
    return jsonify({'expense_types': formatted_expense_types})


# Route to fetch a specific expense type by ID
@expense_types_blueprint.route('/expense_types/<int:expense_type_id>', methods=['GET'])
def get_expense_type_by_id(expense_type_id):
    expense_type = ExpenseTypesController.get_expense_type_by_id(expense_type_id)
    if expense_type:
        return jsonify({'expense_type': {'id': expense_type[0], 'expense_type': expense_type[1], 'inserted_at': expense_type[2], 'updated_at': expense_type[3]} })
    else:
        return jsonify({'error': 'Expense Type not found', 'status_code': 404}), 404


# New route to add a expense type
@expense_types_blueprint.route('/expense_types', methods=['POST'])
def add_expense_type():
    expense_type = request.json.get('expense_type')
    if not expense_type:
        return jsonify({'error': 'Expense type is required', 'status_code': 400}), 400
    
    # Call controller method to add expense type
    new_expense_type = ExpenseTypesController.add_expense_type(expense_type)
    
    if new_expense_type:
        return jsonify({'message': 'Expense type added successfully', 'expense_type': new_expense_type, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add expense type', 'status_code': 500}), 500
    
    
# New route to update a expense type  
@expense_types_blueprint.route('/expense_types/<int:expense_type_id>', methods=['PATCH'])
def update_expense_type_by_id(expense_type_id):
    new_expense_type = request.json.get('expense_type')
    if not new_expense_type:
        return jsonify({'error': 'New expense type is required', 'status_code': 400}), 400

    updated_case = ExpenseTypesController.update_expense_type(expense_type_id, new_expense_type)
    
    if updated_case:
        return jsonify({'message': f'Expense Type with ID {expense_type_id} updated successfully', 'expense_type': updated_case, 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to update expense type with ID {expense_type_id}', 'status_code': 500}), 500



# New route to delete a expense type
@expense_types_blueprint.route('/expense_types/<int:expense_type_id>', methods=['DELETE'])
def delete_expense_type_by_id(expense_type_id):
    deleted_expense_type = ExpenseTypesController.delete_expense_type(expense_type_id)
    
    if deleted_expense_type:
        return jsonify({'message': f'Expense Type with ID {expense_type_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete expense type with ID {expense_type_id}', 'status_code': 500}), 500
