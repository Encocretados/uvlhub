from locust import HttpUser, TaskSet, task

from core.environment.host import get_host_for_locust_testing
from core.locust.common import fake, get_csrf_token


class ViewCommunitiesBehavior(TaskSet):
    @task
    def view_communities(self):
        """
        Simula la visualización de la lista de comunidades.
        """
        response = self.client.get("/community")
        if response.status_code != 200:
            print(f"Failed to load communities: {response.status_code}")

    @task
    def view_single_community(self):
        """
        Simula la visualización de una comunidad específica.
        """
        community_id = 19  # Cambia este ID según tu entorno de pruebas
        response = self.client.get(f"/community/{community_id}")
        if response.status_code != 200:
            print(f"Failed to load community {community_id}: {response.status_code}")


class ManageCommunityBehavior(TaskSet):
    def on_start(self):
        self.login()

    @task
    def create_community(self):
        """
        Simula la creación de una comunidad.
        """
        response = self.client.get("/community/create")
        csrf_token = get_csrf_token(response)

        response = self.client.post(
            "/community/create",
            data={
                "name": fake.company(),
                "description": fake.text(),
                "csrf_token": csrf_token,
            },
        )
        if response.status_code != 200:
            print(f"Failed to create community: {response.status_code}")

    @task
    def edit_community(self):
        """
        Simula la edición de una comunidad.
        """
        community_id = 19  # Cambia este ID según tu entorno de pruebas
        response = self.client.get(f"/community/{community_id}/edit")
        csrf_token = get_csrf_token(response)

        response = self.client.post(
            f"/community/{community_id}/edit",
            data={
                "name": fake.company(),
                "description": fake.text(),
                "csrf_token": csrf_token,
            },
        )
        if response.status_code != 200:
            print(f"Failed to edit community {community_id}: {response.status_code}")

    @task
    def delete_community(self):
        """
        Simula la eliminación de una comunidad.
        """
        community_id = 19  # Cambia este ID según tu entorno de pruebas
        response = self.client.get(f"/community/{community_id}/edit")
        csrf_token = get_csrf_token(response)

        response = self.client.post(
            f"/community/{community_id}/delete", data={"csrf_token": csrf_token}
        )
        if response.status_code != 200:
            print(f"Failed to delete community {community_id}: {response.status_code}")

    def login(self):
        """
        Simula el inicio de sesión antes de realizar acciones protegidas.
        """
        response = self.client.get("/login")
        csrf_token = get_csrf_token(response)

        response = self.client.post(
            "/login",
            data={
                "email": "user1@example.com",
                "password": "1234",
                "csrf_token": csrf_token,
            },
        )
        if response.status_code != 200:
            print(f"Login failed: {response.status_code}")


class CommunityUser(HttpUser):
    tasks = [ViewCommunitiesBehavior, ManageCommunityBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
