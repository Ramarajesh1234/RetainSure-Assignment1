from flask import Blueprint, request, jsonify
from models import get_all_users, get_user_by_id, create_user, update_user, delete_user
import json
from werkzeug.security import generate_password_hash
import re

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify([dict(u) for u in users])

@users_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(dict(user))
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json(force=True)
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not all([name, email, password]):
        return jsonify({'error': 'Missing fields'}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': 'Invalid email format'}), 400
    if len(password) < 6:
        return jsonify({'error': 'Password too short'}), 400
    hashed_password = generate_password_hash(password)
    create_user(name, email, hashed_password)
    return jsonify({'message': 'User created'}), 201

@users_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json(force=True)
    name = data.get('name')
    email = data.get('email')
    if not all([name, email]):
        return jsonify({'error': 'Missing fields'}), 400
    if update_user(user_id, name, email):
        return jsonify({'message': 'User updated'})
    return jsonify({'error': 'Invalid data'}), 400

@users_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    delete_user(user_id)
    return jsonify({'message': f'User {user_id} deleted'}) 