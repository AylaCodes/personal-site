from os import getenv

from dotenv import load_dotenv
from sanic import Sanic

from blueprints.bp_main import main
from blueprints.bp_uploads import uploads

load_dotenv()

app = Sanic("main-site")
app.config.FORWARDED_SECRET = getenv("SANIC_ID")

blueprints = [main, uploads]

for bp in blueprints:
    app.blueprint(bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, fast=True, access_log=False)
