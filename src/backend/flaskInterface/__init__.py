import os
from flask import Flask
from .routes import api
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    
    if test_config is None:
        # Load configuration from config.py
        app.config.from_pyfile("config.py")
    else:
        # Load test config if passed in
        app.config.update(test_config)

    # Register blueprints
    app.register_blueprint(api)

    #Create instance folder if it doesn't exist
    if not os.path.exists(app.config["INSTANCE_FOLDER_PATH"]):
        os.makedirs(app.config["INSTANCE_FOLDER_PATH"])

    return app

app = create_app()

