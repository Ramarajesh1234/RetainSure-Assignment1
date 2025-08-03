from db import get_db

# User model functions (to be expanded)
def get_all_users():
    db = get_db()
    return db.execute('SELECT * FROM users').fetchall()

def get_user_by_id(user_id):
    db = get_db()
    return db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()

def create_user(name, email, password):
    db = get_db()
    db.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
    db.commit()

def update_user(user_id, name=None, email=None):
    db = get_db()
    if name and email:
        db.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
        db.commit()
        return True
    return False

def delete_user(user_id):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    return True 