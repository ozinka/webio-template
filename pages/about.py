from pywebio.output import put_text, clear

from auth import api_login_required


@api_login_required
def page_about():
    clear('content')
    put_text("Welcome to the About Page!", scope='content')