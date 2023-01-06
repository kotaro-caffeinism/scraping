from flask_box import app
import utils
import pprint

val = utils.scrape()[0]["headline"]
pprint.pprint(val)

@app.route("/")
def index():
  return val
  # return "Hello World"