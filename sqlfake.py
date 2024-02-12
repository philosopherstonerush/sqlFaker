from flask import Flask
from logic import parse_ddl_script, generate_data
from flask import request
import sys

app = Flask(__name__)


@app.route("/fake", methods=["POST"])
def get_parse_self():
    data = request.get_json()
    script = data["script"]
    action = data["action"]
    if action == "parse":
        parse = parse_ddl_script(script, True)
        return parse
    elif action == "generate":
        custom_data = data["custom_data"]
        generated_data = generate_data(script, custom_data, 10, True)
        return generated_data
    else:
        return None