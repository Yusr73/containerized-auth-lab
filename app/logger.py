import logging
from pathlib import Path

# Ensure logs folder exists
Path("/logs").mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename="/logs/security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(event_type, username, message):
    logging.info(f"{event_type} | {username} | {message}")
