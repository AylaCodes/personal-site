import json

import arrow

from pathlib import Path

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, html
from jinja2 import Environment, FileSystemLoader

config = json.loads((Path("html/templates/main.json")).read_text())

# Jinja
environment = Environment(loader=FileSystemLoader(Path("html/templates")))
template_main = environment.get_template("main.jinja")
template_about = environment.get_template("about.jinja")
template_projects = environment.get_template("projects.jinja")
template_contact = environment.get_template("contact.jinja")

# Sanic
main = Blueprint("main", host="wolfie.space")

@main.route("/")
async def home_main(request: Request) -> HTTPResponse:
    return html(template_main.render(active="home", **config))

@main.route("/about")
async def about_page(request: Request) -> HTTPResponse:
    return html(template_about.render(
        active="about",
        birth_date=arrow.get(870262176).humanize(),
        **config
        )
    )

@main.route("/projects")
async def projects_page(request: Request) -> HTTPResponse:
    return html(template_projects.render(
        active="projects",
        **config
        )
    )

@main.route("/contact")
async def contact_page(request: Request) -> HTTPResponse:
    return html(template_contact.render(
        active="contact",
        **config
        )
    )
