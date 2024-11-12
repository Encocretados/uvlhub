from flask import render_template, redirect, session, url_for, request
from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import DeveloperSingUpForm, SignupForm, LoginForm
from app.modules.auth.services import AuthenticationService
from app.modules.profile.services import UserProfileService


authentication_service = AuthenticationService()
user_profile_service = UserProfileService()


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template("auth/signup_form.html", form=form, error=f'Email {email} in use')

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template("auth/signup_form.html", form=form, error=f'Error creating user: {exc}')

        # Log user
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if authentication_service.login(form.email.data, form.password.data):
            if current_user.is_developer:
                session['is_developer'] = True
            else:
                session['is_developer'] = False
            return redirect(url_for('public.index'))

        return render_template("auth/login_form.html", form=form, error='Invalid credentials')

    return render_template('auth/login_form.html', form=form)


@auth_bp.route("/signup/developer", methods=["GET", "POST"])
def show_developer_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = DeveloperSingUpForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template("auth/developer_signup_form.html", form=form, error=f'Email {email} in use')

        try:
            user = authentication_service.create_with_profile(**form.data, is_developer=True)
        except Exception as exc:
            return render_template("auth/developer_signup_form.html", form=form, error=f'Error creating user: {exc}')

        login_user(user, remember=True)
        session['is_developer'] = True
        return redirect(url_for('public.index'))

    return render_template("auth/developer_signup_form.html", form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    session.pop('is_developer', None)
    return redirect(url_for('public.index'))
