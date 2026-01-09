# app/__init__.py
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    from app.config import Config
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # ✅ 设置登录视图
    login_manager.login_view = 'routes.login'
    login_manager.login_message = "Please log in to access this page."

    # user_loader
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # ✅ 注册蓝图
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # ✅ 添加根路径路由
    @app.route('/')
    def index():
        return redirect(url_for('routes.login'))

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