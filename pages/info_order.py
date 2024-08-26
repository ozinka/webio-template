from pywebio.input import TEXT, NUMBER
from pywebio.output import use_scope, put_markdown, put_button, put_text
from pywebio.pin import put_input, pin

from auth import api_login_required


@api_login_required
@use_scope('content', clear=True)
def page_info_order(id: int):


    def search_order():
        put_text(f'Searching for Order with ID {pin.order_id}...', scope='content')

    put_input('order_id', type=NUMBER)
    put_button('Search', onclick=lambda: search_order())

    # data = input_group("Order Info", [
    #     input("Order ID", name="order_id", required=True)
    #     ], cancelable=True)

def search_oder():

    return None