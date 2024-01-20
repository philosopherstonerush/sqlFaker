from flask import Flask
from logic import parse_ddl_script
from flask import request

app = Flask(__name__)


@app.route("/fake", methods=["POST"])
def get_parse_self():
    data = request.get_json()
    script = data["script"]
    parse = parse_ddl_script(script, True)
    return parse
