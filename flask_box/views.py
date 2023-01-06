from flask import render_template
from flask_box import app
import utils
import pprint

elms = utils.scrape()
# val = utils.scrape()[0]["headline"]
# pprint.pprint(val)

@app.route("/")
def index():
  return render_template(
    'index.html', elms = elms
  )
  # return "Hello World"