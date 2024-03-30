from flask import jsonify, request
from datetime import datetime
from app.db import db  # Import the SQLAlchemy instance

def check_token(token):
    # token = request.headers.get('User-Token')

    if not token:
        return jsonify({'error': 'Unauthorized Request', 'status_code': 401}), 401

    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_tokens WHERE token = %s", (token,))
    token_data = cursor.fetchone()

    cursor.close()
    connection.close()

    if not token_data:
        return jsonify({'error': 'Invalid Authentication Token', 'token':token_data ,'status_code': 401}), 401

    # Check token expiration
    expiration_date = token_data[2]  # Assuming expiration_date is the third column
    current_time = datetime.now()
    if expiration_date < current_time:
        return jsonify({'error': 'Authentication Token Expired', 'status_code': 401}), 401

    return None

def register_middleware(app):
    @app.before_request
    def before_request():
        result = check_token("sdkoskdomoewokokso23o2k3230jiwejiweji32")
        if result:
            return result  # Return error response if authorization fails
