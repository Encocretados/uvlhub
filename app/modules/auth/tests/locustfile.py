from locust import HttpUser, TaskSet, task , between
from core.locust.common import get_csrf_token, fake
from core.environment.host import get_host_for_locust_testing
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ACCESS_TOKEN_EXPIRES = 3600  

def generate_access_token(user_id):
    expiration = datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRES)
    token = jwt.encode({"user_id": user_id, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token

class TokenLoadTest(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(1, 5)  

    @task(1)
    def generate_token(self):
        """Simula la generación de un token."""
        response = self.client.post("/login", json={
            "email": "test@example.com",
            "password": "password123"
        })
        if response.status_code == 200:
            print("Token generado correctamente")
        else:
            print(f"Error al generar token: {response.status_code}")

    @task(2)
    def validate_token(self):
        """Simula la validación de un token generado previamente."""
        
        token = generate_access_token(user_id=1)

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.get("/protected-api", headers=headers)
        if response.status_code == 200:
            print("Token válido validado correctamente")
        elif response.status_code == 401:
            print("Token inválido detectado")
        else:
            print(f"Error inesperado: {response.status_code}")

    @task(1)
    def missing_token(self):
        """Prueba qué sucede cuando falta un token en la solicitud."""
        response = self.client.get("/protected-api")
        if response.status_code == 401:
            print("Solicitud sin token correctamente rechazada")
        else:
            print(f"Error inesperado: {response.status_code}")

    @task(2)
    def expired_token(self):
        """Prueba el comportamiento con un token expirado."""
        expiration = datetime.now() - timedelta(seconds=10)  
        token = jwt.encode({"user_id": 1, "exp": expiration}, SECRET_KEY, algorithm="HS256")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.get("/protected-api", headers=headers)
        if response.status_code == 401:
            print("Token expirado correctamente rechazado")
        else:
            print(f"Error inesperado: {response.status_code}")

    @task(1)
    def invalid_token(self):
        """Prueba el comportamiento con un token inválido."""
        token = "invalid.token.example"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.get("/protected-api", headers=headers)
        if response.status_code == 401:
            print("Token inválido correctamente rechazado")
        else:
            print(f"Error inesperado: {response.status_code}")

class SignupBehavior(TaskSet):
    def on_start(self):
        self.signup()

    @task
    def signup(self):
        response = self.client.get("/signup")
        csrf_token = get_csrf_token(response)

        response = self.client.post("/signup", data={
            "email": fake.email(),
            "password": fake.password(),
            "csrf_token": csrf_token
        })
        if response.status_code != 200:
            print(f"Signup failed: {response.status_code}")


class LoginBehavior(TaskSet):
    def on_start(self):
        self.ensure_logged_out()
        self.login()

    @task
    def ensure_logged_out(self):
        response = self.client.get("/logout")
        if response.status_code != 200:
            print(f"Logout failed or no active session: {response.status_code}")

    @task
    def login(self):
        response = self.client.get("/login")
        if response.status_code != 200 or "Login" not in response.text:
            print("Already logged in or unexpected response, redirecting to logout")
            self.ensure_logged_out()
            response = self.client.get("/login")

        csrf_token = get_csrf_token(response)

        response = self.client.post("/login", data={
            "email": 'user1@example.com',
            "password": '1234',
            "csrf_token": csrf_token
        })
        if response.status_code != 200:
            print(f"Login failed: {response.status_code}")


class AuthUser(HttpUser):
    tasks = [SignupBehavior, LoginBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
