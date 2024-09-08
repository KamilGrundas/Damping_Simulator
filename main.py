import flet as ft
#from flet_app.views.home_view import home_view
from flet_app.views.test_view import home_view
from i18n.language import language


def main(page: ft.Page):
    page.title = "Moja Aplikacja Flet"
    home_view(page)
    page.update()


ft.app(target=main)
