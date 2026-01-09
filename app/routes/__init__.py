# app/routes/__init__.py
from flask import Blueprint

bp = Blueprint('routes', __name__)

# ✅ 关键修复：导入所有子路由模块
from . import auth
from . import books