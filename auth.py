import hashlib
from functools import wraps
from config import config
import jwt
import datetime
import json
from pywebio.session import run_js, eval_js

USERS = config.users
SECRET_KEY = config.config['secret_key']

print(json.dumps(USERS, indent=4))
print(json.dumps(config.config, indent=4))


def authenticate(username, password):
    if username in USERS and USERS[username]['password'] == hashlib.sha256(password.encode()).hexdigest():
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
