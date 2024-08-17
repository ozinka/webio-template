from pywebio.output import clear_scope, use_scope, style, put_markdown

from pages.home import page_home
from pages.settings import *
from pages.users.users import *
from pages.delete_order import *
from pages.copy_db import *

menu_items = [
    {'id': 'home', 'title': 'Home', 'fas': 'fa-home', 'func': page_home, 'role': 'user'},
    {'id': 'delete_order', 'title': 'Delete Order', 'fas': 'fa-edit', 'func': page_delete_order, 'role': 'user'},
    {'id': 'copy_db', 'title': 'Copy DB', 'fas': 'fa-copy', 'func': page_copy_db, 'role': 'user'},
    {'id': '-', 'title': '----', 'fas': None, 'func': None, 'role': 'admin'},
    {'id': 'users', 'title': 'Users', 'fas': 'fa-users', 'func': page_users, 'role': 'admin'},
    {'id': 'settings', 'title': 'Settings', 'fas': 'fa-gear', 'func': page_settings, 'role': 'admin'},
]

active_style = 'color: #ffaaaa; font-weight: bold;'


def set_menu_active(id: str):
    for i in menu_items:
        if i.get('id') == id:
            add_menu_item(i.get('id'), True)
        else:
            add_menu_item(i.get('id'), False)


def add_menu_item(id: str, is_active=False):
    i = get_menu_item_by_id(menu_items, id)
    with use_scope(id):
        clear_scope()
        if i.get('fas'):
            if is_active:
                put_markdown(f'<i class="fas {i.get('fas')}"></i> - {i.get('title')}').style(active_style).onclick(
                    i.get('func'))
            else:
                put_markdown(f'<i class="fas {i.get('fas')}"></i> - {i.get('title')}').onclick(i.get('func'))
        else:
            put_markdown(f'{i.get('title')}')


def get_menu_item_by_id(menu_items, item_id):
    """Gets a menu item by its ID.

    Args:
      menu_items: A list of dictionaries representing menu items.
      item_id: The ID of the menu item to find.

    Returns:
      The dictionary representing the menu item with the given ID, or None if not found.
    """
    return next((item for item in menu_items if item['id'] == item_id), None)
