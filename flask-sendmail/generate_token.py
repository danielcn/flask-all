
import secrets

def generate_unique_link():
    return secrets.token_urlsafe()