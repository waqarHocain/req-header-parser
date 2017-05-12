from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    os = request.user_agent.platform
    lang = request.accept_languages[0][0]

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return jsonify(
            ipaddress=ip,
            language=lang,
            software=os
            )
