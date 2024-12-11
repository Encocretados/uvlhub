from locust import HttpUser, task, between
import random
from gevent import monkey
monkey.patch_all(thread=False)

class ApiLoadTest(HttpUser):
    # Definir el tiempo entre cada tarea
    wait_time = between(1, 5)

    # Tarea para probar el endpoint "/api/datasets"
    @task
    def get_datasets(self):
        response = self.client.get("/api/datasets")
        if response.status_code == 200:
            print("Datasets retrieved successfully")
        else:
            print(f"Failed to retrieve datasets: {response.status_code}")

    # Tarea para probar el endpoint "/api/dataset/<id>"
    @task(2)  # Esta tarea tiene el doble de peso que la anterior
    def get_single_dataset(self):
        dataset_id = 1  # Asumimos que el ID del dataset es 1
        response = self.client.get(f"/api/dataset/{dataset_id}")
        if response.status_code == 200:
            print(f"Dataset {dataset_id} retrieved successfully")
        else:
            print(f"Failed to retrieve dataset {dataset_id}: {response.status_code}")


class UnsyncedDatasetLoadTest(HttpUser):
    wait_time = between(1, 3)

    # Simulamos que el usuario obtiene un dataset no sincronizado
    @task
    def get_unsynchronized_dataset(self):
        dataset_id = random.randint(1, 100)  # Simulamos un ID de dataset aleatorio entre 1 y 100
        response = self.client.get(f"/dataset/unsynchronized/{dataset_id}/")
        if response.status_code == 200:
            print(f"Dataset no sincronizado {dataset_id} obtenido correctamente.")
        else:
            print(f"Fallo al obtener dataset no sincronizado {dataset_id}: {response.status_code}")
            

class SyncDatasetLoadTest(HttpUser):
    wait_time = between(1, 3)

    # Simulamos que el usuario solicita la sincronización de datasets
    @task
    def synchronize_datasets(self):
        dataset_id = random.randint(1, 100)  # Simulamos un ID de dataset aleatorio entre 1 y 100
        payload = {"datasetId": dataset_id}
        
        # Realizamos una solicitud POST para sincronizar datasets
        response = self.client.post("/dataset/synchronize_datasets", json=payload)
        if response.status_code == 200:
            print(f"Dataset {dataset_id} sincronizado correctamente.")
        else:
            print(f"Fallo al sincronizar dataset {dataset_id}: {response.status_code}")