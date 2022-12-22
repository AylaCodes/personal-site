import re
import json

import arrow

from pathlib import Path

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, html, redirect
from jinja2 import Environment, FileSystemLoader

config = json.loads((Path("html/templates/image.json")).read_text())

# Jinja
environment = Environment(loader=FileSystemLoader(Path("html/templates")))
template_image = environment.get_template("image.jinja")

# Sanic
uploads = Blueprint("uploads", host="uploads.wolfie.space")

@uploads.route("/")
async def home_uploads(request: Request) -> HTTPResponse:
    return redirect("/images/Image_Missing")

@uploads.route("/images/<file:ext>")
async def image_file(request: Request, file: str, ext: str) -> HTTPResponse:
    return redirect(f"{config['cdn_url']}/images/{file}.{ext}")

@uploads.route("/images/<img:str>")
async def image(request: Request, img: str) -> HTTPResponse:
    image_url = f"{config['cdn_url']}/images/{img}.png"

    # Vast majority of images I upload have unix timestamps simply in the filename
    timestamp = re.search("[0-9]+", img)
    if not timestamp:
        timestamp = "at an unknown time"
    else:
        timestamp = arrow.get(int(timestamp.group())).humanize()

    return html(
        template_image.render(
            file_name=img,
            url=image_url,
            timestamp=timestamp.capitalize(),
            **config
        )
    )
