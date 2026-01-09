# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # ✅ 修复：正确加载配置
    from app.config import Config
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # 添加 user_loader
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # 注册蓝图
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # 创建测试用户
    with app.app_context():
        db.create_all()
        from app.models import User
        if not User.query.filter_by(email='test@example.com').first():
            user = User(email='test@example.com')
            user.set_password('test123')
            db.session.add(user)
            db.session.commit()

    return app