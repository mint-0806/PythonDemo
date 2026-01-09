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

# app/__init__.py
# ... 保持原有代码不变 ...

# ✅ 新增：添加 user_loader 回调
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))