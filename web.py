from logging import debug
from flask import Flask
from flask.templating import render_template

from dashboard import create_dash_app

web = Flask(__name__)

create_dash_app(web)

@web.route("/")
def main_page():
    return render_template ("index.html")  


web.run(debug=True, host="0.0.0.0")