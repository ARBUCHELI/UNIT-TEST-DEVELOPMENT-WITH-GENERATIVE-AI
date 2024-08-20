from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# This is a mock database of users with their roles
users_db = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'user': {'password': 'userpass', 'role': 'user'}
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = users_db.get(username)
    # Simple authentication (passwords should be hashed in production)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
        return redirect(url_for('index'))
    return 'Invalid credentials', 401

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'username' in session:
        return f'Hello, {session["username"]}!'
    return 'You are not logged in.'

@app.route('/admin')
def admin_panel():
    # Vulnerable access control: no role check
    if 'username' in session:
        return 'Admin Panel - only for admins'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)