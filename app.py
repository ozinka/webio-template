from pywebio import start_server, config
from pywebio.output import *
from pywebio.pin import *


@config(theme="dark")
def main():
    put_row(
        [put_scope("left-navbar"), None, put_scope("content")], size="200px 50px 85%"
    )
    with use_scope("left-navbar"):
        put_grid(
            [
                [
                    put_text("TypeSense Search Gui Demo").style(
                        "background:#d90368; color:#ffffff; text-align: center; font-weight: bold; font-size: 15pt"
                    ),
                    put_markdown("#### For End User"),
                    put_markdown("- Search").onclick(None),
                    put_markdown("#### For Admin"),
                    put_markdown("- Check Schema").onclick(None),
                    put_markdown("- Add New Record").onclick(None),
                    put_markdown("----"),
                    put_input("email", placeholder="your email"),
                    put_button(
                        "Subscribe for Updates",
                        color="success",
                        small=True,
                        onclick=None,
                    ),
                ]
            ],
            direction="column",
        )


if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
