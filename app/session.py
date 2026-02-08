import secrets

# token -> {username, role}
SESSIONS = {}

def create_session(username, role):
    token = secrets.token_hex(32)
    SESSIONS[token] = {
        "username": username,
        "role": role
    }
    return token

def get_session(token):
    return SESSIONS.get(token)
