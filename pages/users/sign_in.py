from pywebio.input import input_group, input
from pywebio.output import toast, use_scope
from pywebio.session import run_js

import auth

@use_scope('content')
def page_sign_in():
    while True:
        data = input_group("Login", [
            input("Username", name="username", required=True),
            input("Password", name="password", type="password", required=True)
        ])

        username = data["username"]
        password = data["password"]

        if auth.authenticate(username, password):
            token = auth.create_token(username)
            run_js(f"localStorage.setItem('auth_token', '{token}')")
            run_js("window.location.reload()")
            break
        else:
            toast(content="Invalid username or password 🔔", duration=2, position='center', color='warn')