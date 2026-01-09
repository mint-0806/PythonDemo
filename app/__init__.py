# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)

    # 注册蓝图（重要！）
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app