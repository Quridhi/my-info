from flet import *
def main(page:Page):
    page.window.width=250
    page.window.height=470
    page.color="#bfa6c2"
    page.window.title_bar_hidden=True
    page.add(
        Text(value="wellcome to this app"),
        Text(value="this app developed by QURAIDY"),
        Image(src="assets/logo.png",width=230)
    )


    page.update()

app(main)
