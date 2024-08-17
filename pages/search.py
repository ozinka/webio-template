from pywebio.output import put_text, clear

from auth import api_login_required


@api_login_required
def page_search():
    clear('content')
    put_text("Welcome to the Search Page!", scope='content')
