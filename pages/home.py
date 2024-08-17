from pywebio.output import put_text, clear

from auth import api_login_required



@api_login_required
def page_home():
    clear('content')

    from functions import set_menu_active
    set_menu_active('home')

    put_text("Welcome to the Home Page!", scope='content')
    put_text("Welcome to the Home Page!", scope='content')
    put_text("Welcome to the Home Page!", scope='content')
    put_text("Welcome to the Home Page!", scope='content')
    put_text("Welcome to the Home Page!", scope='content')
    put_text("Welcome to the Home Page!", scope='content')