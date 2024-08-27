from pywebio import start_server, config
from pywebio.session import set_env
from menu import show_app


@config(theme="dark")
def main():
    set_env(title="Miki-Here Automation")
    show_app()


if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
