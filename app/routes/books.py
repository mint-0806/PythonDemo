from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Book
from app.routes import bp


@bp.route('/books', methods=['GET', 'POST'])
@login_required
def books():
    if request.method == 'POST':
        # 上传书籍
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(f"uploads/{filename}")
            book = Book(title=filename, filename=filename, user_id=current_user.id)
            db.session.add(book)
            db.session.commit()
            flash('书籍上传成功！')
        return redirect(url_for('books.books'))

    # 显示书籍列表
    books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', books=books)

# app/routes/books.py
# ... 保持原有代码不变 ...

# ✅ 新增：添加根路径路由
@bp.route('/')
@login_required
def index():
    return redirect(url_for('books.books'))  # 重定向到书籍列表