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
template_about = environment.get_template("about.jinja")

# Sanic
about = Blueprint("about", host="wolfie.space")

@about.route("/about")
async def about_page(request: Request) -> HTTPResponse:
    return html(template_about.render(
            active="about",
            birth_date=arrow.get(870262176).humanize(),
            **config
        )
    )
