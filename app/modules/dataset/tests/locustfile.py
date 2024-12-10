from locust import HttpUser, TaskSet, between, task
from core.locust.common import get_csrf_token
from core.environment.host import get_host_for_locust_testing


class RateDatasetBehavior(TaskSet):

    def on_start(self):
        """Simula el inicio de sesión antes de cualquier tarea."""
        self.login()

    @task(1)
    def rate_dataset(self):
        """Simula la calificación de un dataset."""
        dataset_id = 1  # Ajusta el ID del dataset según sea necesario
        rating_value = 4  # Valor de calificación
        with self.client.get(
            f"/dataset/{dataset_id}", name="View Dataset", catch_response=True
        ) as response:
            csrf_token = get_csrf_token(response)
            if csrf_token:
                rating_data = {
                    "rating": rating_value,
                    "csrf_token": csrf_token,
                }
                with self.client.post(
                    f"/datasets/{dataset_id}/rate",
                    data=rating_data,
                    name="Rate Dataset",
                    catch_response=True,
                ) as response:
                    if response.status_code == 200 and "success" in response.text:
                        response.success()
                    else:
                        response.failure("Failed to rate dataset")
            else:
                response.failure("Failed to get CSRF token")

    def login(self):
        """Simula el inicio de sesión."""
        with self.client.get(
            "/login", name="Login Page", catch_response=True
        ) as response:
            csrf_token = get_csrf_token(response)
            if csrf_token:
                login_data = {
                    "username": "user1@example.com",
                    "password": "1234",
                    "csrf_token": csrf_token,
                }
                with self.client.post(
                    "/login", data=login_data, name="Login", catch_response=True
                ) as response:
                    if response.status_code == 200 and "Welcome" in response.text:
                        response.success()
                    else:
                        response.failure("Login failed")
            else:
                response.failure("Failed to get CSRF token")


class RateDatasetUser(HttpUser):
    """Simula usuarios que califican datasets."""

    tasks = [RateDatasetBehavior]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()
