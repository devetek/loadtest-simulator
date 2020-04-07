from locust import TaskSet, task, between
from data.atreus import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        # Home
        for i in range(len(STATIC_DATA["home"])):
            self.client.get(STATIC_DATA["home"][i])
