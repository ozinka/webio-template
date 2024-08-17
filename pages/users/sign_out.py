from pywebio.output import put_text, clear
import auth


def page_sign_out():
    clear()
    auth.logout()