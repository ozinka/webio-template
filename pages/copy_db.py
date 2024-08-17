from pywebio.output import put_text, clear

from auth import api_login_required


@api_login_required
def page_copy_db():
    clear('content')

    from functions import set_menu_active
    set_menu_active('copy_db')

    put_text("Welcome to the Copy DB Page!", scope='content')