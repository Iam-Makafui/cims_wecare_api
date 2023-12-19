from flask import Flask, jsonify, request
from datetime import datetime
from app.db import mysql

def check_token():
    token = request.headers.get('User-Token')

    if not token:
        return jsonify({'error': 'Unauthorized Request', 'status_code': 401}), 401

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM api_tokens WHERE token = %s", (token,))
    token_data = cursor.fetchone()

    if not token_data:
        cursor.close()
        return jsonify({'error': 'Invalid Authentication Token', 'status_code': 401}), 401

    # Check token expiration
    expiration_date = token_data[2]  # Assuming expiration_date is the fourth column
    current_time = datetime.now()
    if expiration_date < current_time:
        cursor.close()
        return jsonify({'error': 'Authentication Token Expired', 'status_code': 401}), 401

    cursor.close()
    return None

def register_middleware(app):
    @app.before_request
    def before_request():
        result = check_token()
        if result:
            return result  # Return error response if authorization fails