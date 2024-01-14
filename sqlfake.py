from flask import Flask
from logic import parse_ddl_script
from flask import request
import json
import sys

app = Flask(__name__)


@app.route("/fake", methods=["POST"])
def get_parse_self():
    data = request.get_json()
    script = data["script"]
    parse = parse_ddl_script(script)
    return parse
