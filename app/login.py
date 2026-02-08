import psycopg2
import bcrypt

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
        return False, None

    stored_hash, role = user

    if bcrypt.checkpw(password.encode(), stored_hash.encode()):
        return True, role

    return False, None
