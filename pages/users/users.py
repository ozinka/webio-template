from pywebio.output import put_text, clear, put_html


def page_users():
    clear('content')

    from functions import set_menu_active
    set_menu_active('users')

    put_html('<h1 class="text-center mt-0 mb-4">Users management</h1>', scope='content')