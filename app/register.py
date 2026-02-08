import psycopg2 #Python library to talk to PostgreSQL
import bcrypt
from logger import log_event
# Connect to DB
conn = psycopg2.connect(  #conn → connection object to your database
    dbname="authdb",
    user="authuser",
    password="authpass",
    host="auth_db"
)
cur = conn.cursor() #cursor object → allows executing SQL queries from Python

def register_user(username, password, role="user"):
    # Hash password
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    try:
        cur.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", #%s → placeholders → prevents SQL injection
            (username, password_hash, role)
        )
        conn.commit()
        print(f"User {username} registered successfully.")
        log_event("REGISTER", username, f"Role: {role}")
    except Exception as e:
        print("Error:", e)
        log_event("REGISTER_FAIL", username, str(e)) 
    
