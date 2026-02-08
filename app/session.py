import secrets
from logger import log_event


# token -> {username, role}
SESSIONS = {}

def create_session(username, role):
    token = secrets.token_hex(32)
    SESSIONS[token] = {
        "username": username,
        "role": role
    }
    log_event("SESSION_CREATE", username, f"Token: {token[:6]}...")
    return token

def get_session(token):
    return SESSIONS.get(token)

def logout(token):
    if token in SESSIONS:
        username = SESSIONS[token]["username"]
        log_event("SESSION_DELETE", username, f"Token: {token[:6]}...")
        del SESSIONS[token]