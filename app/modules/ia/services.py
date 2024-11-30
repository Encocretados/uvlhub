import os
import jwt
from flask_login import login_user
from flask_login import current_user
from datetime import datetime, timedelta
from app.modules.auth.models import User
from app.modules.auth.repositories import UserRepository
from app.modules.profile.models import UserProfile
from app.modules.profile.repositories import UserProfileRepository
from core.configuration.configuration import uploads_folder_name
from core.services.BaseService import BaseService
from flask import request
