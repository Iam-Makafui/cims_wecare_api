from flask import Blueprint, jsonify, request
from app.controllers.query_controller import QueryController

query_blueprint = Blueprint('query', __name__)

@query_blueprint.route('/query', methods=['POST'])
def query_database():
    """Handle natural language queries."""
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' in request body", "status_code": 400}), 400
    
    query = data['query']
    visualize = data.get('visualize', False)
    
    response, status_code = QueryController.process_query(query, visualize)
    return jsonify(response), status_code

@query_blueprint.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "status_code": 200}), 200