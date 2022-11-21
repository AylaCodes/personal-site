from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, text

main = Blueprint("main", host="wolfie.space")

@main.route("/")
async def home_main(request: Request) -> HTTPResponse:
    return text("Hello, wolfie!")
