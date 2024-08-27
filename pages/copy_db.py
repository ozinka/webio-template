from pywebio.output import put_text, clear, put_html, put_button, use_scope

from auth import api_login_required


@use_scope('content', clear=False)
def copy_db():
    put_text('DB copied')


@api_login_required
@use_scope('content', clear=True)
def page_copy_db():
    clear('content')

    from functions import set_menu_active
    set_menu_active('copy_db')

    put_html('<h1 class="text-center mt-0 mb-4">Copy DB: PROD->DEV</h1>', scope='content')
    put_button('Copy DB from PROD to Dev', onclick=copy_db)
