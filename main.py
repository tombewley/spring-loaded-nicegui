from argparse import ArgumentParser
from nicegui import ui

from settings import SERVER_PORT, STORAGE_SECRET
import user

# Option to skip login page
parser = ArgumentParser()
parser.add_argument("--no_login", action="store_true")
args = parser.parse_args()
page_type = ui.page if args.no_login else user.page


@user.login_page
def login():
    user.login_form().on("success", lambda: ui.navigate.to("/"))


@page_type("/", title="Page Title")
def main_page():
    with ui.header(elevated=True).classes("justify-center w-full"):
        ui.label("😊 Hello, World!").classes("text-2xl")
    
    ui.label("This is a simple web app using NiceGUI and Descope.").classes("text-lg")


ui.run(favicon="😊", port=SERVER_PORT, storage_secret=STORAGE_SECRET)
