import os
from datetime import datetime, timedelta

from flask import redirect, render_template, request, session, url_for
from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import DeveloperSingUpForm, LoginForm, SignupForm
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
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template(
                "auth/signup_form.html", form=form, error=f"Email {email} in use"
            )

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template(
                "auth/signup_form.html", form=form, error=f"Error creating user: {exc}"
            )

        # Log user
        login_user(user, remember=True)
        return redirect(url_for("public.index"))

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = authentication_service.login(form.email.data, form.password.data)
        if user:
            token = generate_access_token(user.id)
            login_user(user)
            if current_user.is_developer:
                session["is_developer"] = True
            else:
                session["is_developer"] = False
            response = redirect(url_for("public.index"))
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
    response = redirect(url_for("public.index"))
    response.set_cookie("access_token", "", expires=0)
    return response
