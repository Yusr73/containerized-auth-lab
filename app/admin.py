from session import get_session

def admin_action(token):
    session = get_session(token)
    if not session:
        return "Unauthorized"

    if session["role"] != "admin":
        return "Forbidden"

    return "Admin action executed"
