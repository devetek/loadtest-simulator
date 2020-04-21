from locust import TaskSet, task, between
from data.promomicrofrontend import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        # Home
        for i in range(len(STATIC_DATA["ramadhan"])):
            self.client.get(STATIC_DATA["ramadhan"][i])
