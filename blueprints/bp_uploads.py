import json

import arrow

from pathlib import Path

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, text, html
from jinja2 import Environment, FileSystemLoader

config = json.loads((Path("html/templates/image.json")).read_text())

# Jinja
environment = Environment(loader=FileSystemLoader(Path("html/templates")))
template_image = environment.get_template("image.jinja")

# Sanic
uploads = Blueprint("uploads", host="uploads.wolfie.space")

@uploads.route("/")
async def home_uploads(request: Request) -> HTTPResponse:
    return text("Hello, upload!")

@uploads.route("/images/<img:str>")
async def image(request: Request, img: str) -> HTTPResponse:
    image_file = Path(f"html/images/{img}.png")

    if not image_file.is_file():
        img = "Image Missing"
        image_url = f"https://{request.host}/images/Image_Missing.png"
        timestamp = arrow.now.humanize()
    else:
        image_url = f"https://{request.host}/images/{img}.png"
        timestamp = arrow.get(image_file.stat().st_mtime).humanize()

    return html(
        template_image.render(
            file_name=img,
            url=image_url,
            timestamp=timestamp.capitalize(),
            **config
        )
    )
