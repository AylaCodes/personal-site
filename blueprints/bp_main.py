import json

from pathlib import Path

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, text, html
from jinja2 import Environment, FileSystemLoader

config = json.loads((Path("html/templates/main.json")).read_text())

# Jinja
environment = Environment(loader=FileSystemLoader(Path("html/templates")))
template_main = environment.get_template("main.jinja")

# Sanic
main = Blueprint("main", host="wolfie.space")

@main.route("/")
async def home_main(request: Request) -> HTTPResponse:
    return html(template_main.render(**config))
