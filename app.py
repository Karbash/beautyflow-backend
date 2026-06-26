from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
import os
import yaml

from database import create_tables
from routes import api

app = Flask(__name__)
CORS(app)

swagger_path = os.path.join(os.path.dirname(__file__), "swagger.yaml")
template = {}
if os.path.exists(swagger_path):
    with open(swagger_path, "r") as f:
        try:
            template = yaml.safe_load(f) or {}
        except Exception:
            template = {}

Swagger(app, template=template) if template else Swagger(app)

create_tables()
app.register_blueprint(api)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug, host="0.0.0.0", port=port)
