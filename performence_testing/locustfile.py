from locust import task, HttpUser
import random

class MemeUser(HttpUser):
    """Desc"""
    token = None

    def on_start(self):
        response = self.client.post(
            "/auth",
            json={'login': 'win', 'password': 'win'}
        )
        self.token = response.json()['token']

    @task(1)
    def get_all_memes(self):
        self.client.get("/ibs/index.jsp")

    @task(3)
    def get_one_meme(self):
        self.client.get("/ibs/index.jsp")

