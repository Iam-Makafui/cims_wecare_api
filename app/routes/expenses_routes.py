from flask import Blueprint, jsonify, request
from app.controllers.expenses_controller import ExpensesController

expenses_blueprint = Blueprint('expenses', __name__)

# route to fetch all expenses
@expenses_blueprint.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = ExpensesController.get_all_expenses()
    
    formatted_expenses = []
    for expense in expenses:
        formatted_expenses.append({
            'expense_type': expense[0],
            'id': expense[1],
            'description': expense[2],
            'amount': expense[3],
            'date': expense[4],
            'inserted_at': expense[5],
            'firstname': expense[6],
            'lastname': expense[7]
        })
    
    return jsonify({'expenses': formatted_expenses})


# Route to fetch a specific expense by ID
@expenses_blueprint.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense_by_id(expense_id):
    expense = ExpensesController.get_expense_by_id(expense_id)
    if expense:
        return jsonify({'expense': {'expense_type': expense[0], 'id': expense[1], 'description': expense[2], 'amount': expense[3], 'date': expense[4], 'inserted_at': expense[5], 'firstname': expense[6], 'lastname': expense[7]} })
    else:
        return jsonify({'error': 'Expense not found', 'status_code': 404}), 404


# New route to add a expense
@expenses_blueprint.route('/expenses', methods=['POST'])
def add_case():
    required_fields = ['expense_type_id', 'description', 'amount', 'date', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    expense_type_id = data['expense_type_id']
    description = data['description']
    amount = data['amount']
    date = data['date']
    user_id = data['user_id']

    # Call controller method to add expense
    new_expense = ExpensesController.add_expense(expense_type_id, description, amount, date, user_id)
    
    if new_expense:
        return jsonify({'message': 'Expense added successfully', 'expenses': new_expense, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add expense', 'status_code': 500}), 500
    
    
# New route to update a expense
@expenses_blueprint.route('/expenses', methods=['PATCH'])
def update_case():
    required_fields = ['expense_id', 'expense_type_id', 'description', 'amount', 'date', 'user_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    expense_id = data['expense_id']
    expense_type_id = data['expense_type_id']
    description = data['description']
    amount = data['amount']
    date = data['date']
    user_id = data['user_id']
    

    # Call controller method to update expense
    update_expense = ExpensesController.update_expense(expense_id, expense_type_id, description, amount, date, user_id)
    
    if update_expense:
        return jsonify({'message': 'Expense Updated Successfully', 'case': update_expense, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to update expense', 'status_code': 500}), 500
    


# New route to delete a expense
@expenses_blueprint.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expenses_by_id(expense_id):
    deleted_expense = ExpensesController.delete_expense(expense_id)
    
    if deleted_expense:
        return jsonify({'message': f'Expense with ID {expense_id} deleted successfully', 'status_code': 200}), 200
    else:
        return jsonify({'error': f'Failed to delete expense with ID {expense_id}', 'status_code': 500}), 500
