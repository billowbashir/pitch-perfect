from flask import render_template
from . import auth
from .forms import LoginForm

@main.route('/login/')
def login():
    login_form = LoginForm()

    return render_template('auth/login.html', login_form=login_form)
