import email
import imaplib
import os
import re
import smtplib
from datetime import datetime, timedelta
from email.header import decode_header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import jwt
from flask import request
from flask_login import current_user, login_user

from app.modules.auth.models import User
from app.modules.auth.repositories import UserRepository
from app.modules.profile.models import UserProfile
from app.modules.profile.repositories import UserProfileRepository
from core.configuration.configuration import uploads_folder_name
from core.services.BaseService import BaseService

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ACCESS_TOKEN_EXPIRES = int(os.getenv("ACCESS_TOKEN_EXPIRES", 3600))  # 1 hora


def generate_access_token(user_id: int):
    expiration = datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRES)
    token = jwt.encode(
        {"user_id": user_id, "exp": expiration}, SECRET_KEY, algorithm="HS256"
    )
    return token


class AuthenticationService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
        self.user_profile_repository = UserProfileRepository()

    def login(self, email, password, remember=True):
        user = self.repository.get_by_email(email)
        if user is not None and user.check_password(password):
            login_user(user, remember=remember)
            return user
        return user

    def get_user(self, email, password, remember=True):
        user = self.repository.get_by_email(email)
        if user is not None and user.check_password(password):
            return user
        return user

    def correct_credentials(self, email, password, remember=False):
        user = self.repository.get_by_email(email)
        if user is not None and user.check_password(password):
            return True
        return False

    def is_email_available(self, email: str) -> bool:
        return self.repository.get_by_email(email) is None

    # Modificación en la creación de un usuario en el servicio de autenticación
    def create_with_profile(self, **kwargs):
        try:
            email = kwargs.pop("email", None)
            password = kwargs.pop("password", None)
            name = kwargs.pop("name", None)
            surname = kwargs.pop("surname", None)
            is_developer = kwargs.pop("is_developer", False)

            if not email:
                raise ValueError("Email is required.")
            if not password:
                raise ValueError("Password is required.")
            if not name:
                raise ValueError("Name is required.")
            if not surname:
                raise ValueError("Surname is required.")

            user_data = {
                "email": email,
                "password": password,
                "is_developer": is_developer,  # Aquí se pasa el valor de is_developer
            }

            profile_data = {
                "name": name,
                "surname": surname,
            }

            user = self.create(commit=False, **user_data)
            profile_data["user_id"] = user.id
            self.user_profile_repository.create(**profile_data)
            self.repository.session.commit()
        except Exception as exc:
            self.repository.session.rollback()
            raise exc
        return user

    def update_profile(self, user_profile_id, form):
        if form.validate():
            updated_instance = self.update(user_profile_id, **form.data)
            return updated_instance, None

        return None, form.errors

    def get_authenticated_user(self) -> User | None:
        if current_user.is_authenticated:
            return current_user
        return None

    def get_authenticated_user_profile(self) -> UserProfile | None:
        if current_user.is_authenticated:
            return current_user.profile
        return None

    def temp_folder_by_user(self, user: User) -> str:
        return os.path.join(uploads_folder_name(), "temp", str(user.id))

    def generate_token(self, user_id: int):
        return generate_access_token(user_id)

    def get_token_from_cookie(self):
        return request.cookies.get("access_token")

    def verify_access_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def send_email(self, target_email, random_key):
        sender_email = "uvlhub.reply@gmail.com"
        receiver_email = target_email
        password = str(os.getenv("UVLHUB_EMAIL_PASSWORD"))
        subject = f"[UVLHUB] Your key is {random_key}!"
        body = f"""
                <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                        }}
                        .bold {{
                            font-weight: bold;
                        }}
                    </style>
                </head>
                <body>
                    <p>Hello,</p>
                    <p>Thank you for using <span class="bold">UVLHUB</span>!</p>
                    <p>To complete your authentication process, please use the following <span class="bold">
                    authentication key</span>:</p>
                    <p class="bold">{random_key}</p>
                    <p>Please enter this key in the authentication form to proceed. If you did not request this key or
                    believe this is an error, please contact our support team immediately.</p>
                    <p>For your security, this key is valid for a limited time only.</p>
                    <p>Best regards,</p>
                    <p><span class="bold">The UVLHUB Team</span></p>
                    <p><a href="mailto:support@uvlhub.com">Contact us</a> if you need assistance.</p>
                </body>
                </html>
                """
        message = MIMEMultipart()
        message["From"] = target_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # TLS port
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully to " + str(target_email) + "!")
        except Exception as e:
            print(f"Error: {e}")

    def get_validation_email_info(self, verbose=False):
        username = "uvlhub.reply@gmail.com"
        password = str(os.getenv("UVLHUB_EMAIL_PASSWORD"))
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")
        _, messages = mail.search(None, "FROM", '"uvlhub.reply@gmail.com"')
        email_ids = messages[0].split()
        res = {}

        if email_ids:
            latest_email_id = email_ids[-1]
            _, msg_data = mail.fetch(latest_email_id, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    # Decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    res["Subject"] = subject
                    # Decode the sender
                    from_ = msg.get("From")
                    res["From"] = from_
                    # Decode the key
                    key = re.sub(r"[^0-9]", "", subject)
                    res["Key"] = key

                    if verbose:
                        print(f"Subject: {subject}")
                        print(f"From: {from_}")
                        print(f"Key: {key}")

        else:
            print("No emails found from uvlhub.reply@gmail.com.")

        # Logout and close the connection
        mail.logout()
        return res

    def get_validation_email_key(self):
        res = self.get_validation_email_info(False)
        return res["Key"]
