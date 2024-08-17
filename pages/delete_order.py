from pywebio.output import put_text, clear

from auth import api_login_required


@api_login_required
def page_delete_order():
    clear('content')

    from functions import set_menu_active
    set_menu_active('delete_order')

    put_text("Welcome to the Delete Order Page!", scope='content')