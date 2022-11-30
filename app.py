from os import getenv

from dotenv import load_dotenv
from sanic import Sanic
from sanic.blueprints import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, text

from blueprints.bp_main import main
from blueprints.bp_uploads import uploads
from blueprints.bp_about import about

load_dotenv()

app = Sanic("main-site")
app.config.FORWARDED_SECRET = getenv("SANIC_ID")

blueprints = [main, uploads, about]

for bp in blueprints:
    app.blueprint(bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, workers=8, access_log=False)
