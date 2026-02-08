from session import get_session
from logger import log_event

def admin_action(token):
    session = get_session(token)
    if not session:
        log_event("ADMIN_ACCESS_FAIL", "UNKNOWN", "Unauthorized token")
        return "Unauthorized"

    if session["role"] != "admin":
        log_event("ADMIN_ACCESS_FAIL", session["username"], "Forbidden")
        return "Forbidden"
    log_event("ADMIN_ACTION", session["username"], "Executed admin action")

    return "Admin action executed"
