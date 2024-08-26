from pywebio.output import put_text, clear, put_html

from auth import api_login_required


@api_login_required
def page_settings():
    clear('content')

    from functions import set_menu_active
    set_menu_active('settings')

    put_html('<h1 class="text-center mt-0 mb-4">Settings</h1>', scope='content')
