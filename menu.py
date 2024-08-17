from pywebio.input import input, input_group
from pywebio.output import put_row, put_scope, use_scope, put_grid, put_markdown, put_image, put_html, put_button, \
    toast, popup, put_buttons, close_popup
from pywebio.session import run_js

from pages.home import *
from pages.users.sign_out import *

from functions import menu_items, add_menu_item, set_menu_active


def show_header():
    # Add Awesome Fonts
    put_html(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">')

    # Load Logo
    with open('static/images/ava2_64.png', "rb") as file:
        img_data = file.read()

    # Create Header Item List
    data = [
        put_image(img_data).style('border-radius: 5px'),
        put_text('Miki-Care Automation').style('flex-grow: 1; text-align: center;'),
    ]

    # Add Sign Out button if authenticated
    if auth.is_authenticated():
        data.append(put_row([put_text(auth.get_authenticated_user()).style('margin-right: 10px;'),
                             put_button('Sign Out',
                                        onclick=page_sign_out,
                                        color='success').style('flex-grow: 1; text-align: center; width: 100px'),
                             ]).style('flex-grow: 0; text-align: right; align-items: center;')
                    )

    put_row(data, size="64px 85% 100px").style("background-color: #112; padding: 5px; align-items: center;")


def show_popup(msg):
    popup('Info', [
        put_text(msg),
        put_buttons(['Close'], onclick=lambda _: close_popup())
    ])


def show_menu(active='home'):
    clear()
    if not auth.is_authenticated():
        show_header()
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
                show_menu()
                break
            else:
                toast(content="Invalid username or password 🔔", duration=2, position='center', color='warn')
    else:
        show_header()
        # Menu
        put_row([put_scope("left-navbar"),
                 None,
                 put_scope("content")], size="150px 30px 85%").style(
            'margin-top: 20px;')

        with use_scope("left-navbar"):
            clear()
            put_grid(
                [[put_scope(i.get('id')) for i in menu_items]],
                direction="column",
            )

            page_home()

