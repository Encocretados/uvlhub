import os
from flask_login import login_user
from flask_login import current_user

from app.modules.auth.models import User
from app.modules.auth.repositories import UserRepository
from app.modules.profile.models import UserProfile
from app.modules.profile.repositories import UserProfileRepository
from core.configuration.configuration import uploads_folder_name
from core.services.BaseService import BaseService
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class AuthenticationService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
        self.user_profile_repository = UserProfileRepository()

    def login(self, email, password, remember=True):
        user = self.repository.get_by_email(email)
        if user is not None and user.check_password(password):
            login_user(user, remember=remember)
            return True
        return False

    def correct_credentials(self, email, password, remember=False):
        user = self.repository.get_by_email(email)
        if user is not None and user.check_password(password):
            return True
        return False

    def is_email_available(self, email: str) -> bool:
        return self.repository.get_by_email(email) is None

    def create_with_profile(self, **kwargs):
        try:
            email = kwargs.pop("email", None)
            password = kwargs.pop("password", None)
            name = kwargs.pop("name", None)
            surname = kwargs.pop("surname", None)

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
                "password": password
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

    def send_email(self, target_email, random_key):
        sender_email = "uvlhub.reply@gmail.com"    # TODO Create the gmail account
        receiver_email = target_email                           # TODO Find a way to get the user email
        password = "fdqqdofcvxvcjgit "                                           # TODO Add gmail account password
        subject = "[UVLHUB] Your key is {random_key}!"
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
                    <p>We are excited to help you secure your account.</p>
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
                print("Email sent successfully to "+str(target_email)+"!")
        except Exception as e:
            print(f"Error: {e}")
