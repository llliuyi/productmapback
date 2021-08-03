from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    db.init_app(app)

    from app.api import bp as api_bp
    #从app 的api的__init__中导出蓝图BP
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app import model
