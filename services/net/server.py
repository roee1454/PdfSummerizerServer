from os import environ
from asyncio import Future
from dotenv import load_dotenv
from flask import Flask, Blueprint

load_dotenv()

def init_blueprints():
    return [Blueprint('index', __name__, url_prefix="/"), Blueprint('generate', __name__, url_prefix="/generate")]


def init_server():
    app = Flask(__name__)
    blueprints = init_blueprints()

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.run(port=environ.get("PORT", 8000), host="0.0.0.0", debug=True)
    print(f"App is live at: http://localhost:{environ.get("SERVER_PORT")}")
        
            