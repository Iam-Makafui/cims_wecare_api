from flask import Blueprint, jsonify, request
from app.controllers.members_controller import MembersController

members_blueprint = Blueprint('members', __name__)

# route to fetch all members
@members_blueprint.route('/members', methods=['GET'])
def get_members():
    members = MembersController.get_all_members()
    
    formatted_members = []
    for member in members:
        formatted_members.append({
            'id': member[0],
            'member_id': member[1],
            'name': member[2],
            'inserted_at': member[3],
            'updated_at': member[4]
        })
    
    return jsonify({'members': formatted_members})


# Route to fetch a specific member by ID
@members_blueprint.route('/members/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    member = MembersController.get_member_by_id(member_id)
    if member:
        return jsonify({'member': {'id': member[0], 'member_id': member[1], 'name': member[2], 'inserted_at': member[3], 'updated_at': member[4]} })
    else:
        return jsonify({'error': 'Member not found', 'status_code': 404}), 404