from flask import Flask
from db import close_db
from routes.users import users_bp
from routes.auth import auth_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)
app.teardown_appcontext(close_db)

@app.route('/')
def home():
    return "User Management System"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)