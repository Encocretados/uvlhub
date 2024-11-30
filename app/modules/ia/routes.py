import os
from flask import render_template, redirect, session, url_for, request
from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import DeveloperSingUpForm, SignupForm, LoginForm
from app.modules.auth.services import AuthenticationService, generate_access_token
from app.modules.profile.services import UserProfileService
from datetime import datetime, timedelta
