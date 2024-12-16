import os
from datetime import datetime, timedelta

import pyotp
from flask import (make_response, redirect, render_template, request, session,
                   url_for)
from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import (DeveloperSingUpForm, EmailValidationForm,
                                    LoginForm, SignupForm)
from app.modules.auth.services import (AuthenticationService,
                                       generate_access_token)
from app.modules.profile.services import UserProfileService

authentication_service = AuthenticationService()
user_profile_service = UserProfileService()


ACCESS_TOKEN_EXPIRES = int(os.getenv("ACCESS_TOKEN_EXPIRES", 3600))  # 1 hora


def get_token_from_cookie():
    return request.cookies.get("access_token")


@auth_bp.route("/protected-api", methods=["GET"])
def protected_api():
    # Obtener el token de la cookie
    token = get_token_from_cookie()
    if token:
        # Verificar el token
        user_id = AuthenticationService.verify_access_token(token)
        if user_id:
            # Token válido, puedes proceder con la lógica de la API
            return {"message": "Token valid", "user_id": user_id}
        else:
            return {"message": "Invalid token"}, 401
    else:
        return {"message": "Token missing"}, 401


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = SignupForm()
    if form.validate_on_submit():
        email = request.form["email"]
        password = request.form["password"]
        print(f"Email: {email}")
        print(f"Password: {password}")
        if not authentication_service.is_email_available(email):
            return render_template(
                "auth/signup_form.html", form=form, error=f"Email {email} in use"
            )

        try:
            authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template(
                "auth/signup_form.html", form=form, error=f"Error creating user: {exc}"
            )

        # Log user
        response = make_response(redirect(url_for("auth.email_validation")))
        session["email"] = email
        session["password"] = password
        return response

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = request.form["email"]
        password = request.form["password"]
        session["email"] = email
        session["password"] = password
        if authentication_service.correct_credentials(email, password):
            user_no_login = authentication_service.get_user(
                form.email.data, form.password.data
            )
            token = generate_access_token(user_no_login.id)
            if user_no_login.is_developer:
                session["is_developer"] = True
            else:
                session["is_developer"] = False
            response = make_response(redirect(url_for("auth.email_validation")))
            expires = datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRES)
            response.set_cookie(
                "access_token", token, httponly=True, expires=expires, secure=True
            )
            return response

        return render_template(
            "auth/login_form.html", form=form, error="Invalid credentials"
        )

    return render_template("auth/login_form.html", form=form)


@auth_bp.route("/signup/developer", methods=["GET", "POST"])
def show_developer_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = DeveloperSingUpForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template(
                "auth/developer_signup_form.html",
                form=form,
                error=f"Email {email} in use",
            )

        try:
            user = authentication_service.create_with_profile(
                **form.data, is_developer=True
            )
        except Exception as exc:
            return render_template(
                "auth/developer_signup_form.html",
                form=form,
                error=f"Error creating user: {exc}",
            )

        login_user(user, remember=True)
        session["is_developer"] = True
        return redirect(url_for("public.index"))

    return render_template("auth/developer_signup_form.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    session.pop("is_developer", None)
    session.pop("email", None)
    session.pop("password", None)
    response = make_response(redirect(url_for("public.index")))
    response.set_cookie("access_token", "", expires=0)
    return response


@auth_bp.route("/email_validation", methods=["GET", "POST"])
def email_validation():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    email = session.get("email", None)
    password = session.get("password", None)
    if not email or not password:
        return redirect(url_for("auth.login"))

    form = EmailValidationForm()

    if request.method == "POST":
        key = int(form.key.data.strip())
        if key == int(session.get("key")):
            authentication_service.login(email, password)
            response = make_response(redirect(url_for("public.index")))
            session.pop("email", None)
            session.pop("password", None)
            return response

        return render_template(
            "auth/email_validation_form.html",
            form=form,
            key=key,
            error="The key does not match",
        )

    if request.method == "GET":
        random_key = pyotp.TOTP(str(os.getenv("SECRET_CODE_GENERATOR"))).now()
        session["key"] = random_key
        authentication_service.send_email(email, random_key)
    return render_template("auth/email_validation_form.html", form=form, email=email)
