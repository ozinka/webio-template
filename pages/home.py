from pywebio.output import put_text, clear, put_html, put_row, use_scope, put_markdown

from auth import api_login_required

prod_db_connection = True
dev_db_connection = False

prod_web_connection = True
dev_web_connection = False


@api_login_required
@use_scope('content', clear=True)
def page_home():

    from functions import set_menu_active
    set_menu_active('home')

    # Website
    put_html('<h2 class="text-center mt-0 mb-4 font-italic">Website</h2>')
    data = [put_text('Production: ')]
    if prod_web_connection:
        data.append(put_markdown(f'<i class="fas fa-check"></i>').style('color: #77ff77;'))
    else:
        data.append(put_markdown(f'<i class="fas fa-xmark"></i>').style('color: #ffaaaa;'))
    put_row(data, size='330px auto')

    data = [put_text('Development: ')]
    if dev_web_connection:
        data.append(put_markdown(f'<i class="fas fa-check"></i>').style('color: #77ff77;'))
    else:
        data.append(put_markdown(f'<i class="fas fa-xmark"></i>').style('color: #ffaaaa;'))
    put_row(data, size='330px auto')

    # Database
    put_html('<h2 class="text-center mt-4 mb-4 font-italic">Database</h2>')
    data = [put_text('Production: ')]
    if prod_db_connection:
        data.append(put_markdown(f'<i class="fas fa-check"></i>').style('color: #77ff77;'))
    else:
        data.append(put_markdown(f'<i class="fas fa-xmark"></i>').style('color: #ffaaaa;'))
    put_row(data, size='330px auto')

    data = [put_text('Development: ')]
    if dev_db_connection:
        data.append(put_markdown(f'<i class="fas fa-check"></i>').style('color: #77ff77;'))
    else:
        data.append(put_markdown(f'<i class="fas fa-xmark"></i>').style('color: #ffaaaa;'))
    put_row(data, size='330px auto')

