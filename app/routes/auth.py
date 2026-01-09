# app/routes/auth.py
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models import User
from app.routes import bp
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # ✅ 添加 BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')  # ✅ 添加 remember_me 字段
    submit = SubmitField('Login')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)  # ✅ 使用 remember_me
            return redirect(url_for('books.books'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))