from pywebio.output import put_text, clear

from auth import api_login_required


@api_login_required
def page_settings():
    clear('content')

    from functions import set_menu_active
    set_menu_active('settings')

    put_text("Welcome to the Settings Page!", scope='content')
