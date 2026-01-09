# app/routes/__init__.py
from flask import Blueprint

bp = Blueprint('routes', __name__)

# 导入所有路由模块（确保 books.py 被加载）
from . import books