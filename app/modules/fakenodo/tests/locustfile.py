from locust import HttpUser, TaskSet, between, task


class FakenodoTaskSet(TaskSet):

    @task(1)
    def test_connection(self):
        self.client.get("/fakenodo/api/test_connection")

    @task(2)
    def create_fakenodo(self):
        data = {"dataset_id": 1}
        self.client.post("/fakenodo/api/fakenodos", json=data)

    @task(2)
    def upload_file(self):
        data = {"dataset_id": 1, "feature_model_id": 1}
        fakenodo_id = 1
        self.client.post(f"/fakenodo/api/{fakenodo_id}/files", data=data)

    @task(1)
    def publish_fakenodo(self):
        fakenodo_id = 1
        self.client.put(f"/fakenodo/api/{fakenodo_id}/publish")

    @task(1)
    def get_fakenodo(self):
        fakenodo_id = 1
        self.client.get(f"/fakenodo/api/{fakenodo_id}")

    @task(1)
    def get_doi(self):
        fakenodo_id = 1
        self.client.get(f"/fakenodo/api/{fakenodo_id}/doi")

    @task(1)
    def get_all_fakenodos(self):
        self.client.get("/fakenodo/api/fakenodos")

    @task(1)
    def delete_fakenodo(self):
        fakenodo_id = 1
        self.client.delete(f"/fakenodo/api/{fakenodo_id}")


class FakenodoUser(HttpUser):
    host = "http://127.0.0.1:5000"
    tasks = [FakenodoTaskSet]
    wait_time = between(1, 5)
