from logger import log_event
import psycopg2
import bcrypt
from session import create_session

conn = psycopg2.connect(
    dbname="authdb",
    user="authuser",
    password="authpass",
    host="auth_db"
)
cur = conn.cursor()
def get_user(username):
    cur.execute(
        "SELECT password_hash, role FROM users WHERE username = %s",
        (username,)
    )
    return cur.fetchone()
def login(username, password):
    user = get_user(username)
    if not user:
        log_event("LOGIN_FAIL", username, "User not found")
        print("Login failed: user not found")
        return None

    stored_hash, role = user

    if bcrypt.checkpw(password.encode(), stored_hash.encode()):
        token = create_session(username, role)
        log_event("LOGIN_SUCCESS", username, f"Role: {role}, Token: {token[:6]}...")  # Shows token prefix only (don’t log full token — security best practice)
        print(f"Login successful: {username}")
        return token
    
    log_event("LOGIN_FAIL", username, "Incorrect password")
    print("Login failed: incorrect password")
    return None
