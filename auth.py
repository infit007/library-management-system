from typing import Optional, Dict
import hashlib
import time
import hmac
import base64

SECRET_KEY = "your-secret-key"  # In production, use environment variables
tokens: Dict[str, int] = {}  # Store active tokens: {token: member_id}

def generate_token(member_id: int) -> str:
    timestamp = str(int(time.time()))
    message = f"{member_id}:{timestamp}"
    signature = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).digest()
    token = base64.urlsafe_b64encode(f"{message}:{signature}".encode()).decode()
    tokens[token] = member_id
    return token

def verify_token(token: str) -> Optional[int]:
    return tokens.get(token)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
