from pywebio.output import put_text, clear


def page_users():
    clear('content')

    from functions import set_menu_active
    set_menu_active('users')

    put_text("Welcome to the Users Page!", scope='content')