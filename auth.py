import hashlib
from functools import wraps

import jwt
import datetime

from pywebio.session import run_js, eval_js

# Secret key for JWT
SECRET_KEY = "your-secret-key"

# Mock user database
users = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
    "ozi": hashlib.sha256("1".encode()).hexdigest(),
}


def authenticate(username, password):
    if username in users and users[username] == hashlib.sha256(password.encode()).hexdigest():
        return True
    return False


def create_token(username):
    expiration = datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=8)
    return jwt.encode({"username": username, "exp": expiration}, SECRET_KEY, algorithm="HS256")


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["username"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def logout():
    run_js("localStorage.removeItem('auth_token')")
    run_js("window.location.reload()")


def is_authenticated():
    token = eval_js("localStorage.getItem('auth_token')")
    if token:
        username = verify_token(token)
        return username is not None
    return False


def get_authenticated_user():
    token = eval_js("localStorage.getItem('auth_token')")
    if token:
        username = verify_token(token)
        return username
    return None


def api_login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_authenticated():
            return func(*args, **kwargs)
        else:
            return {"error": "Authentication required"}, 401

    return wrapper
