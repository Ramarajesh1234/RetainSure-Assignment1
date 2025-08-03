from flask import Blueprint, request, jsonify
from db import get_db
from werkzeug.security import check_password_hash
import re

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Please provide a name to search'}), 400
    db = get_db()
    users = db.execute('SELECT * FROM users WHERE name LIKE ?', (f'%{name}%',)).fetchall()
    return jsonify([dict(u) for u in users])

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    email = data.get('email')
    password = data.get('password')
    if not all([email, password]):
        return jsonify({'status': 'failed', 'error': 'Missing credentials'}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'status': 'failed', 'error': 'Invalid email format'}), 400
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    if user and check_password_hash(user['password'], password):
        return jsonify({'status': 'success', 'user_id': user['id']})
    return jsonify({'status': 'failed'}), 401 