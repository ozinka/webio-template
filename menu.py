from pywebio.output import put_scope, put_grid, put_image, put_button

from functions import menu_items
from pages.edit_order import page_edit_order
from pages.home import *
from pages.users.sign_out import *
from pages.users.sign_in import page_sign_in


def show_header():
    # Add Awesome Fonts
    put_html(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">')

    # Load Logo
    file_name = 'static/images/ava2_64.png'

    # Create Header Item List
    data = [
        put_image(open(file_name, "rb").read()).style('border-radius: 5px'),
        put_text('Miki-Here Automation').style('flex-grow: 1; font-style: italic;'),
    ]

    # Add Sign Out button if authenticated
    if auth.is_authenticated():
        data.append(put_row([put_text(auth.get_authenticated_user()).style('margin-right: 10px;'),
                             put_button('Sign Out',
                                        onclick=page_sign_out,
                                        color='success').style('flex-grow: 1; text-align: center; width: 100px'),
                             ]).style('flex-grow: 0; text-align: right; align-items: center;')
                    )
    put_scope('header')
    put_row(data, size="100px Auto 200px",scope='header').style("background-color: #111519; padding: 5px; align-items: center;")


def show_app():
    clear()
    show_header()
    if not auth.is_authenticated():
        page_sign_in()
    else:
        # Menu
        put_row([put_scope("left-navbar").style('background-color: #111519;'),
                 None,
                 put_scope("content")], size="150px 30px auto").style(
            'margin-top: 20px;')

        with use_scope("left-navbar"):
            clear()
            put_grid(
                [[put_scope(i.get('id')).style('margin-left: 10px; margin-right: 10px') for i in menu_items]],
                direction="column",
            ).style('margin-top: 65px')

        page_edit_order()
